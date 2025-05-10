import pandas as pd

class DataAnalyzer:
    def __init__(self, config):
        self.file_path = config.get("data_path", "data/trade_data.csv")

    def analyze_performance(self):
        try:
            df = pd.read_csv(self.file_path)
            win_rate = df[df['profit'] > 0].shape[0] / df.shape[0]
            avg_profit = df['profit'].mean()
            return {
                "win_rate": win_rate,
                "average_profit": avg_profit
            }
        except FileNotFoundError:
            return {
                "win_rate": 0,
                "average_profit": 0
            }
