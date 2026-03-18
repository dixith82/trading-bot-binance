import argparse
import sys

from client import BinanceAPIError, BinanceClient, BinanceNetworkError
from logging_config import get_logger
from orders import place_order
from validators import validate_all

log = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True, dest="order_type")
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop-price", type=float, dest="stop_price")

    args = parser.parse_args()

    try:
        params = validate_all(
            args.symbol, args.side, args.order_type,
            args.quantity, args.price, args.stop_price
        )
    except ValueError as e:
        print("Validation error:", e)
        sys.exit(1)

    print("Order Request:", params)

    try:
        client = BinanceClient()
    except Exception as e:
        print("Config error:", e)
        sys.exit(1)

    try:
        result = place_order(client, **params)
    except BinanceAPIError as e:
        print("API Error:", e)
        sys.exit(1)
    except BinanceNetworkError as e:
        print("Network Error:", e)
        sys.exit(1)

    print("Response:", result)

if __name__ == "__main__":
    main()