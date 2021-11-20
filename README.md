# ubub
A (micro)python library for pub-sub messaging for (u)asyncio apps

## A short demo first:

```python
from ubub import Ub

try:
    import uasyncio as asyncio
except ImportError:
    import asyncio


ub = Ub()


async def sender():
    while True:
        await ub.pub("topic", "Ahoj!")
        await asyncio.sleep(1)


async def receiver():
    while True:
        msg = await ub.sub("topic")
        print(msg)
```