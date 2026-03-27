import logging

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
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"API Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Order Error: {str(e)}")
        raise


def format_order_response(order):
    return {
        "orderId": order.get("orderId"),
        "status": order.get("status"),
        "executedQty": order.get("executedQty"),
        "avgPrice": order.get("avgPrice", "N/A")
    }