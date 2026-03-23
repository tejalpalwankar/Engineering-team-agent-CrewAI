import gradio as gr
from accounts import Account

account = None

def create_account(user_id: str, initial_deposit: float):
    global account
    account = Account(user_id, initial_deposit)
    return f"Account created for {user_id} with initial deposit ${initial_deposit:.2f}"

def deposit_funds(amount: float):
    if account:
        account.deposit(amount)
        return f"Deposited ${amount:.2f}. New balance is ${account.balance:.2f}"
    return "No account found."

def withdraw_funds(amount: float):
    if account:
        try:
            account.withdraw(amount)
            return f"Withdrew ${amount:.2f}. New balance is ${account.balance:.2f}"
        except ValueError as e:
            return str(e)
    return "No account found."

def buy_shares(symbol: str, quantity: int):
    if account:
        try:
            account.buy_shares(symbol, quantity)
            return f"Bought {quantity} shares of {symbol}. New balance is ${account.balance:.2f}"
        except ValueError as e:
            return str(e)
    return "No account found."

def sell_shares(symbol: str, quantity: int):
    if account:
        try:
            account.sell_shares(symbol, quantity)
            return f"Sold {quantity} shares of {symbol}. New balance is ${account.balance:.2f}"
        except ValueError as e:
            return str(e)
    return "No account found."

def get_portfolio_value():
    if account:
        return f"Total portfolio value: ${account.get_portfolio_value():.2f}"
    return "No account found."

def get_profit_loss():
    if account:
        return account.report_profit_loss()
    return "No account found."

def get_holdings():
    if account:
        holdings = account.get_holdings()
        return holdings if holdings else "No holdings."
    return "No account found."

def list_transactions():
    if account:
        return account.list_transactions()
    return "No account found."

with gr.Blocks() as demo:
    gr.Markdown("## Trading Account Management System")
    
    with gr.Row():
        user_id = gr.Textbox(label="User ID")
        initial_deposit = gr.Number(label="Initial Deposit", value=1000.0)
        create_btn = gr.Button("Create Account")
    
    create_output = gr.Markdown("")
    
    create_btn.click(create_account, inputs=[user_id, initial_deposit], outputs=create_output)
    
    gr.Markdown("### Deposit Funds")
    deposit_amount = gr.Number(label="Amount to Deposit")
    deposit_btn = gr.Button("Deposit")
    deposit_output = gr.Markdown("")
    
    deposit_btn.click(deposit_funds, inputs=deposit_amount, outputs=deposit_output)
    
    gr.Markdown("### Withdraw Funds")
    withdraw_amount = gr.Number(label="Amount to Withdraw")
    withdraw_btn = gr.Button("Withdraw")
    withdraw_output = gr.Markdown("")
    
    withdraw_btn.click(withdraw_funds, inputs=withdraw_amount, outputs=withdraw_output)
    
    gr.Markdown("### Buy Shares")
    buy_symbol = gr.Textbox(label="Share Symbol (AAPL, TSLA, GOOGL)")
    buy_quantity = gr.Number(label="Quantity")
    buy_btn = gr.Button("Buy Shares")
    buy_output = gr.Markdown("")
    
    buy_btn.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=buy_output)
    
    gr.Markdown("### Sell Shares")
    sell_symbol = gr.Textbox(label="Share Symbol (AAPL, TSLA, GOOGL)")
    sell_quantity = gr.Number(label="Quantity")
    sell_btn = gr.Button("Sell Shares")
    sell_output = gr.Markdown("")
    
    sell_btn.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=sell_output)
    
    gr.Markdown("### Reports")
    report_btn = gr.Button("Get Portfolio Value")
    portfolio_value_output = gr.Markdown("")
    
    report_btn.click(get_portfolio_value, outputs=portfolio_value_output)
    
    profit_loss_btn = gr.Button("Get Profit/Loss")
    profit_loss_output = gr.Markdown("")
    
    profit_loss_btn.click(get_profit_loss, outputs=profit_loss_output)
    
    holdings_btn = gr.Button("Get Holdings")
    holdings_output = gr.Markdown("")
    
    holdings_btn.click(get_holdings, outputs=holdings_output)
    
    transactions_btn = gr.Button("List Transactions")
    transactions_output = gr.Markdown("")
    
    transactions_btn.click(list_transactions, outputs=transactions_output)

demo.launch()