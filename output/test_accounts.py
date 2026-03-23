import unittest
from unittest.mock import patch

from accounts import Account, get_share_price


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('user123', 1000.0)
    
    def test_initialization(self):
        self.assertEqual(self.account.user_id, 'user123')
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.shares, {})
        self.assertEqual(self.account.initial_deposit, 1000.0)
        self.assertEqual(self.account.transactions, [])
    
    def test_deposit(self):
        self.account.deposit(500.0)
        self.assertEqual(self.account.balance, 1500.0)
        self.assertEqual(self.account.transactions[-1], ('Deposit', 500.0))
    
    def test_withdraw_sufficient_funds(self):
        self.account.withdraw(300.0)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(self.account.transactions[-1], ('Withdraw', 300.0))
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(1500.0)
        self.assertEqual(str(context.exception), 'Insufficient funds for withdrawal.')
    
    @patch('accounts.get_share_price')
    def test_buy_shares_sufficient_funds(self, mock_get_price):
        mock_get_price.return_value = 150.0  # AAPL price
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.balance, 1000.0 - 150.0*2)  # 700.0
        self.assertEqual(self.account.shares, {'AAPL': 2})
        self.assertEqual(self.account.transactions[-1], ('Buy', 'AAPL', 2, 150.0))
    
    @patch('accounts.get_share_price')
    def test_buy_shares_insufficient_funds(self, mock_get_price):
        mock_get_price.return_value = 1500.0
        with self.assertRaises(ValueError) as context:
            self.account.buy_shares('AAPL', 1)
        self.assertEqual(str(context.exception), 'Insufficient funds to buy shares.')
    
    @patch('accounts.get_share_price')
    def test_buy_shares_negative_quantity(self, mock_get_price):
        mock_get_price.return_value = 150.0
        with self.assertRaises(ValueError) as context:
            self.account.buy_shares('AAPL', -1)
        self.assertEqual(str(context.exception), 'Quantity must be positive.')
    
    @patch('accounts.get_share_price')
    def test_sell_shares_sufficient(self, mock_get_price):
        mock_get_price.return_value = 150.0
        self.account.buy_shares('AAPL', 5)
        initial_balance = self.account.balance
        self.account.sell_shares('AAPL', 3)
        self.assertEqual(self.account.balance, initial_balance + 150.0*3)
        self.assertEqual(self.account.shares, {'AAPL': 2})
        self.assertEqual(self.account.transactions[-1], ('Sell', 'AAPL', 3, 150.0))
    
    @patch('accounts.get_share_price')
    def test_sell_shares_insufficient(self, mock_get_price):
        mock_get_price.return_value = 150.0
        self.account.buy_shares('AAPL', 2)
        with self.assertRaises(ValueError) as context:
            self.account.sell_shares('AAPL', 5)
        self.assertEqual(str(context.exception), 'Insufficient shares to sell.')
    
    @patch('accounts.get_share_price')
    def test_sell_shares_nonexistent(self, mock_get_price):
        mock_get_price.return_value = 150.0
        with self.assertRaises(ValueError) as context:
            self.account.sell_shares('AAPL', 1)
        self.assertEqual(str(context.exception), 'Insufficient shares to sell.')
    
    @patch('accounts.get_share_price')
    def test_get_portfolio_value(self, mock_get_price):
        mock_get_price.return_value = 150.0
        self.account.buy_shares('AAPL', 4)
        # Balance after buying 4 shares at 150 each: 1000 - 600 = 400
        # Portfolio value = balance + shares value = 400 + 600 = 1000
        self.assertEqual(self.account.get_portfolio_value(), 1000.0)
    
    @patch('accounts.get_share_price')
    def test_calculate_profit_loss(self, mock_get_price):
        mock_get_price.return_value = 150.0
        self.account.buy_shares('AAPL', 4)
        # Initial deposit 1000, portfolio value 1000, profit/loss 0
        self.assertEqual(self.account.calculate_profit_loss(), 0.0)
        # Change price to simulate profit
        mock_get_price.return_value = 200.0
        # Portfolio value: balance 400 + shares 4*200 = 1200, profit 200
        self.assertEqual(self.account.calculate_profit_loss(), 200.0)
    
    def test_get_holdings(self):
        with patch('accounts.get_share_price', return_value=150.0):
            self.account.buy_shares('AAPL', 2)
            self.assertEqual(self.account.get_holdings(), {'AAPL': 2})
    
    @patch('accounts.get_share_price')
    def test_report_profit_loss(self, mock_get_price):
        mock_get_price.return_value = 150.0
        self.account.buy_shares('AAPL', 4)
        mock_get_price.return_value = 200.0
        self.assertEqual(self.account.report_profit_loss(), 'Profit/Loss: $200.00')
    
    def test_list_transactions(self):
        with patch('accounts.get_share_price', return_value=150.0):
            self.account.deposit(100.0)
            self.account.withdraw(50.0)
            self.account.buy_shares('AAPL', 1)
            self.account.sell_shares('AAPL', 1)
            transactions = self.account.list_transactions()
            expected = [
                ('Deposit', 100.0),
                ('Withdraw', 50.0),
                ('Buy', 'AAPL', 1, 150.0),
                ('Sell', 'AAPL', 1, 150.0)
            ]
            self.assertEqual(transactions, expected)


class TestGetSharePrice(unittest.TestCase):
    def test_get_share_price_valid(self):
        self.assertEqual(get_share_price('AAPL'), 150.00)
        self.assertEqual(get_share_price('TSLA'), 700.00)
        self.assertEqual(get_share_price('GOOGL'), 2800.00)
    
    def test_get_share_price_invalid(self):
        with self.assertRaises(ValueError) as context:
            get_share_price('INVALID')
        self.assertEqual(str(context.exception), 'Invalid stock symbol.')


if __name__ == '__main__':
    unittest.main()