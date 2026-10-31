from .inventory_service import InventoryService
from .notification_service import NotificationService
from .order import Order
from .payment_service import PaymentService
from .shipping_service import ShippingService


class OrderFulfillmentFacade:
    def __init__(
        self,
        inventory: InventoryService | None = None,
        payment: PaymentService | None = None,
        shipping: ShippingService | None = None,
        notification: NotificationService | None = None,
    ) -> None:
        self.inventory = inventory if inventory is not None else InventoryService()
        self.payment = payment if payment is not None else PaymentService()
        self.shipping = shipping if shipping is not None else ShippingService()
        self.notification = notification if notification is not None else NotificationService()

    def place_order(self, order: Order) -> list[str]:
        return [
            self.inventory.reserve(order),
            self.payment.charge(order),
            self.shipping.create_shipment(order),
            self.notification.send_confirmation(order),
        ]
