import logging
import os
from dotenv import load_dotenv
from binance.client import Client as BinanceClient
from .validators import validate_order

load_dotenv()

logger = logging.getLogger(__name__)

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    if not api_key or not api_secret:
        raise RuntimeError("API_KEY and API_SECRET must be set in environment or .env")

    client = BinanceClient(api_key, api_secret)

    # Binance Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client


def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
        elif order_type == "LIMIT":
            if price is None:
                raise ValueError("Price is required for LIMIT orders")
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
        else:
            raise ValueError("order_type must be MARKET or LIMIT")

        logger.info(f"Order placed: {order}")
        return order

    except Exception as e:
        logger.error(f"Error placing order: {str(e)}")
        raise


class TradingClient:
    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price=None):
        validate_order(symbol, side, order_type, quantity, price)
        logger.info(f"Placing order: {symbol} {side} {quantity}@{price}")
        # This class is kept as a wrapper; prefer using get_client() + bot.orders.place_order()
        raise NotImplementedError("Use get_client() and bot.orders.place_order() for actual futures orders")

    def cancel_order(self, order_id: str):
        logger.info(f"Cancelling order: {order_id}")
        raise NotImplementedError("Canceling via TradingClient is not implemented in this version")
