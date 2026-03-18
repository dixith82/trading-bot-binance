def validate_all(symbol, side, order_type, quantity, price, stop_price):

    if side not in ["BUY","SELL"]:
        raise ValueError("Invalid side")

    if order_type not in ["MARKET","LIMIT","STOP","STOP_MARKET"]:
        raise ValueError("Invalid order type")

    if quantity <= 0:
        raise ValueError("Quantity must be >0")

    if order_type == "LIMIT" and not price:
        raise ValueError("Price required")

    if order_type in ["STOP","STOP_MARKET"] and not stop_price:
        raise ValueError("Stop price required")

    return {
        "symbol": symbol,
        "side": side,
        "order_type": order_type,
        "quantity": quantity,
        "price": price,
        "stop_price": stop_price
    }