from client import BinanceClient
from logging_config import get_logger

log = get_logger(__name__)

def place_order(client, symbol, side, order_type, quantity, price=None, stop_price=None):

    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    if order_type in ["STOP", "STOP_MARKET"]:
        params["stopPrice"] = stop_price

    try:
        res = client.request("POST", "/fapi/v1/order", params)
        return {
            "success": True,
            "order_id": res.get("orderId"),
            "status": res.get("status"),
            "executedQty": res.get("executedQty"),
            "avgPrice": res.get("avgPrice")
        }
    except Exception as e:
        return {"success": False, "error": str(e)}