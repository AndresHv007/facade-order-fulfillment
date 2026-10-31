from .order import Order
from .order_fulfillment_facade import OrderFulfillmentFacade


class OrderClient:
    def __init__(
        self,
        facade: OrderFulfillmentFacade | None = None,
        *legacy_services: object,
    ) -> None:
        if legacy_services:
            self.facade = OrderFulfillmentFacade(facade, *legacy_services)  # type: ignore[arg-type]
        elif facade is None:
            self.facade = OrderFulfillmentFacade()
        else:
            self.facade = facade

    def place_order(self, order: Order) -> list[str]:
        return self.facade.place_order(order)
