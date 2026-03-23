# accounts.py

class Account:
    def __init__(self, user_id: str, initial_deposit: float):
        self.user_id = user_id
        self.balance = initial_deposit
        self.shares = {}
        self.initial_deposit = initial_deposit
        self.transactions = []

    def deposit(self, amount: float):
        self.balance += amount
        self.transactions.append(("Deposit", amount))

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount
        self.transactions.append(("Withdraw", amount))

    def buy_shares(self, symbol: str, quantity: int):
        price = get_share_price(symbol)
        total_cost = price * quantity
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to buy shares.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.balance -= total_cost
        if symbol in self.shares:
            self.shares[symbol] += quantity
        else:
            self.shares[symbol] = quantity
        self.transactions.append(("Buy", symbol, quantity, price))

    def sell_shares(self, symbol: str, quantity: int):
        if symbol not in self.shares or self.shares[symbol] < quantity:
            raise ValueError("Insufficient shares to sell.")
        price = get_share_price(symbol)
        total_value = price * quantity
        self.shares[symbol] -= quantity
        if self.shares[symbol] == 0:
            del self.shares[symbol]
        self.balance += total_value
        self.transactions.append(("Sell", symbol, quantity, price))

    def get_portfolio_value(self) -> float:
        total_value = self.balance
        for symbol, quantity in self.shares.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def calculate_profit_loss(self) -> float:
        return self.get_portfolio_value() - self.initial_deposit

    def get_holdings(self) -> dict:
        return self.shares

    def report_profit_loss(self) -> str:
        profit_loss = self.calculate_profit_loss()
        return f"Profit/Loss: ${profit_loss:.2f}"

    def list_transactions(self) -> list:
        return self.transactions


def get_share_price(symbol: str) -> float:
    if symbol == "AAPL":
        return 150.00
    elif symbol == "TSLA":
        return 700.00
    elif symbol == "GOOGL":
        return 2800.00
    else:
        raise ValueError("Invalid stock symbol.")