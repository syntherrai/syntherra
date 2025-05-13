import unittest
from strategies.ai_trend_follow import AITrendFollow

class TestStrategy(unittest.TestCase):
    def test_signal_output(self):
        strategy = AITrendFollow("models/trading_model.pkl")
        mock_data = [{'close': p} for p in range(100, 131)]  # generate dummy prices

        signal = strategy.generate_signal(mock_data)
        self.assertIn(signal, ["BUY", "SELL", "HOLD"])

if __name__ == '__main__':
    unittest.main()
