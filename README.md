# ubub

![ubub](./logo.png)

A (micro)python library for pub-sub messaging for (u)asyncio apps

## Simple demo:

```python
from ubub import Ub

try:
    import uasyncio as asyncio
except ImportError:
    import asyncio

ub = Ub()

async def sender(msg="Ahoj!", delay=1):
    while True:
        ub.pub("topic", msg)
        await asyncio.sleep(delay)


async def receiver():
    while True:
        msg = await ub.sub("topic")
        print("Message:", msg)


async def main():
    # Subscribers
    asyncio.create_task(receiver())

    # Senders
    asyncio.create_task(sender())
    asyncio.create_task(sender("Ciao", 0.5))

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main())
```

## Contribution notes

### Design

Logo - Font [Assistant](https://fonts.google.com/specimen/Assistant) Extra Light 200