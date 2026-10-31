from order_fulfillment.inventory_service import InventoryService
from order_fulfillment.notification_service import NotificationService
from order_fulfillment.order import Order
from order_fulfillment.order_client import OrderClient
from order_fulfillment.order_fulfillment_facade import OrderFulfillmentFacade
from order_fulfillment.payment_service import PaymentService
from order_fulfillment.shipping_service import ShippingService


def test_client_places_order_through_facade():
    facade = OrderFulfillmentFacade(
        InventoryService(),
        PaymentService(),
        ShippingService(),
        NotificationService(),
    )
    client = OrderClient(facade)
    order = Order("O-100", "SKU-42", 250.0, "Zapopan")

    steps = client.place_order(order)

    assert client.facade is facade
    assert steps == [
        "inventory:reserved:SKU-42",
        "payment:charged:250.00",
        "shipping:created:Zapopan",
        "notification:sent:O-100",
    ]
