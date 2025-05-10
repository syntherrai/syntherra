CONFIG = {
    "api_key": "YOUR_API_KEY",
    "api_secret": "YOUR_API_SECRET",
    "trading_pair": "BTC/USDT",
    "exchange": "Binance",
    "strategy": {
        "type": "trend_following",
        "parameters": {
            "short_window": 50,
            "long_window": 200
        }
    },
    "risk_management": {
        "max_drawdown": 0.1,
        "stop_loss": 0.02,
        "take_profit": 0.05
    }
}
