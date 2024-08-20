from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):

    HOURLY_WAGE: float = 15.0
    SHIFT_TYPE = "full-time"



