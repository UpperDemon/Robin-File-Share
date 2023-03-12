from typing import Union

from pyrate_limiter import (BucketFullException, Duration, Limiter,
                            MemoryListBucket, RequestRate)


class RateLimiter:

    def __init__(self) -> None:

        # 2 requests per seconds
        self.second_rate = RequestRate(2, Duration.SECOND)

        # 17 requests per minute.
        self.minute_rate = RequestRate(17, Duration.MINUTE)

        # 1000 requests per hour
        self.hourly_rate = RequestRate(1000, Duration.HOUR)

        # 10000 requests per day
        self.daily_rate = RequestRate(10000, Duration.DAY)

        self.limiter = Limiter(
            self.minute_rate,
            self.hourly_rate,
            self.daily_rate,
            bucket_class=MemoryListBucket,
        )

    async def acquire(self, userid:Union[int, str]) -> bool:

        try:
            self.limiter.try_acquire(userid)
            return False
        except BucketFullException:
            return True
