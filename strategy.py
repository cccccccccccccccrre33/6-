from indicators import get_indicator_data

PAIRS = ["BTC-USDT", "ETH-USDT", "BNB-USDT", "SOL-USDT", "ADA-USDT", "XRP-USDT", "DOGE-USDT"]

def get_signals():
    signals = []
    for pair in PAIRS:
        data = get_indicator_data(pair)
        # Простая логика: если EMA50 > EMA200 → LONG, иначе SHORT
        if data['ema50'] > data['ema200']:
            side = "LONG"
        else:
            side = "SHORT"
        signals.append({
            "pair": pair,
            "side": side,
            "entry": data['close'] * 1.001,  # пример точки входа
            "exit": data['close'] * 0.995,   # пример точки выхода
            "leverage": 5
        })
    return signals
