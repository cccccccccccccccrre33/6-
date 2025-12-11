import pandas as pd
import numpy as np
from ta.trend import EMAIndicator

def get_indicator_data(pair):
    # Заглушка: данные можно брать через OKX API
    close = 100  # пример текущей цены
    ema50 = close * 1.01
    ema200 = close * 0.99
    return {"close": close, "ema50": ema50, "ema200": ema200}
