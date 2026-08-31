portfolio = [
    {"symbol": "AAPL", "shares": 10, "buy_price": 180, "current_price": 195},
    {"symbol": "TSLA", "shares": 5, "buy_price": 220, "current_price": 205},
    {"symbol": "MSFT", "shares": 8, "buy_price": 350, "current_price": 420},
]

total_invested = 0
total_current_value = 0

print("STOCK PORTFOLIO\n")

for stock in portfolio:
    invested = stock["shares"] * stock["buy_price"]
    current_value = stock["shares"] * stock["current_price"]
    profit_loss = current_value - invested
    percentage = (profit_loss / invested) * 100

    total_invested += invested
    total_current_value += current_value

    print(f"{stock['symbol']}")
    print(f"  Shares: {stock['shares']}")
    print(f"  Invested: ${invested:,.2f}")
    print(f"  Current Value: ${current_value:,.2f}")
    print(f"  Profit/Loss: ${profit_loss:,.2f} ({percentage:.2f}%)\n")

total_profit_loss = total_current_value - total_invested
total_percentage = (total_profit_loss / total_invested) * 100

print("PORTFOLIO SUMMARY")
print(f"Total Invested: ${total_invested:,.2f}")
print(f"Current Value: ${total_current_value:,.2f}")
print(f"Total Profit/Loss: ${total_profit_loss:,.2f} ({total_percentage:.2f}%)")