def simulate_trade(balance, price, signal):
    position = 0
    if signal == "BUY" and balance >= price:
        position += 1
        balance -= price
    elif signal == "SELL" and position > 0:
        position -= 1
        balance += price
    return balance, position

# Example usage:
balance, position = simulate_trade(1000, 250, "BUY")
balance, position = simulate_trade(balance, 300, "SELL")
print(f"Final balance: {balance}, position: {position}")
