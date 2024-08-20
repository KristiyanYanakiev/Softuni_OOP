from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    HOURLY_WAGE: float = 12.0
    SHIFT_TYPE = "half-time"
