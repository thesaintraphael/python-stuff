import heapq
import datetime


def email(frequency: datetime.timedelta, details: str):

    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, details


fast_email = email(datetime.timedelta(minutes=15), "Fast email")
slow_email = email(datetime.timedelta(minutes=40), "Slow email")


unified = heapq.merge(fast_email, slow_email)


for _ in range(10):
    print(next(unified))
