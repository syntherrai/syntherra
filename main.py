from config import CONFIG
from strategy import Strategy
from risk_management import RiskManager
from market_data import MarketData
from trade_executor import TradeExecutor

def main():
    market_data = MarketData(CONFIG)
    strategy = Strategy(CONFIG)
    risk_manager = RiskManager(CONFIG)
    executor = TradeExecutor(CONFIG)

    while True:
        data = market_data.fetch()
        signal = strategy.generate_signal(data)

        if risk_manager.evaluate(signal, data):
            executor.execute(signal, data)

if __name__ == "__main__":
    main()
