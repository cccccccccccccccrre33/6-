from indicators import get_indicator_data

PAIRS = ["BTC-USDT", "ETH-USDT", "BNB-USDT", "SOL-USDT", "ADA-USDT", "XRP-USDT", "DOGE-USDT"]

def get_signals():
    signals = []
    for pair in PAIRS:
        data = get_indicator_data(pair)
        side = "LONG" if data['ema50'] > data['ema200'] else "SHORT"
        signals.append({
            "pair": pair,
            "side": side,
            "entry": data['close'] * 1.001,
            "exit": data['close'] * 0.995,
            "leverage": 5
        })
    return signals
