try:
    import uasyncio as asyncio
except ImportError:
    import asyncio


class Ub:
    def __init__(self):
        # Subscribers
        self._t = {}
        # Messages
        self._m = {}

    def pub(self, t, msg):
        self._m[t] = msg

        es = self._t.get(t, [])
        while es:
            e = es.pop()
            self._m[e] = msg
            e.set()

    async def sub(self, t):
        e = asyncio.Event()
        if not t in self._t:
            self._t[t] = []
        self._t[t].append(e)
        await e.wait()
        m = self._m.get(t)
        e.clear()
        del self._m[e]
        return m
