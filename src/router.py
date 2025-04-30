import random
from typing import Literal, cast

Topic = Literal[1, 2, 3, 4, 5]


def router(query: str) -> Topic:
    result = 1 + len(query)
    return cast(Topic, result)
