def validate_order(symbol, side, order_type, quantity, price):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs supported (e.g., BTCUSDT)")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    try:
        quantity = float(quantity)
        if quantity <= 0:
            raise ValueError
    except:
        raise ValueError("Quantity must be a valid positive number")

    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price required for LIMIT order")
        try:
            float(price)
        except:
            raise ValueError("Price must be a valid number")