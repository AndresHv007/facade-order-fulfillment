# Facade Pattern — Order Fulfillment

## Design Overview

- **Facade (`OrderFulfillmentFacade`):** Provides a single `place_order(order)` entry point that coordinates the standard fulfillment sequence across `InventoryService`, `PaymentService`, `ShippingService`, and `NotificationService`.
- **Client (`OrderClient`):** Depends on `OrderFulfillmentFacade` instead of coupling directly to the four subsystem service classes, delegating `place_order(order)` to the Facade.
- **Subsystem Services:** `InventoryService`, `PaymentService`, `ShippingService`, and `NotificationService` remain unmodified and keep their respective domain responsibilities (reserving stock, charging payment, creating shipments, and sending order confirmations).

## Focused Test

`tests/test_order_fulfillment_facade.py` (`test_client_places_order_through_facade`) verifies that `OrderClient` receives an `OrderFulfillmentFacade` instance and executes the complete four-step fulfillment workflow in the expected order.

Run locally with:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Complexity Cost Introduced by the Facade

Introducing `OrderFulfillmentFacade` adds an extra class and indirection layer that centralizes coupling to all four subsystem services. If new fulfillment variations, conditional rules, or extra subsystem calls accumulate inside the Facade over time, it risks evolving into a **God Object** tightly coupled to every subsystem, where changes to underlying service contracts require updating and retesting the Facade.
