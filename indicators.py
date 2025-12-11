import pandas as pd
from ta.trend import EMAIndicator

def get_indicator_data(pair):
    # Заглушка, можно подключить OKX API для реальных данных
    close = 100  # текущая цена
    ema50 = close * 1.01
    ema200 = close * 0.99
    return {"close": close, "ema50": ema50, "ema200": ema200}
