import asyncio
from contextvars import ContextVar, copy_context

var = ContextVar('hi')
var.set('hi')
var.set('by')
var.set('sie')
c = copy_context()
print(list(c.items()))

l = asyncio.new_event_loop()
asyncio.set_event_loop(l)
l.run_until_complete()
