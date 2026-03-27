import argparse
import logging

from bot.client import get_client
from bot.orders import place_order, format_order_response
from bot.validators import validate_order
from bot.logging_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        # Validate input
        validate_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        client = get_client()

        logging.info(f"Request: {vars(args)}")

        # Place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        formatted = format_order_response(order)

        logging.info(f"Response: {formatted}")

        # Output
        print("\n Order Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        print("\n Order Response:")
        print(f"Order ID: {formatted['orderId']}")
        print(f"Status: {formatted['status']}")
        print(f"Executed Qty: {formatted['executedQty']}")
        print(f"Average Price: {formatted['avgPrice']}")

        print("\n Order executed successfully!")

    except Exception as e:
        logging.error(f"CLI Error: {str(e)}")
        print(f"\n Error: {str(e)}")


if __name__ == "__main__":
    main()