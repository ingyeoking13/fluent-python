import asyncio
import contextvars

my_var = contextvars.ContextVar('my_var', default='origin')

# Define a coroutine that sets the value of the context-local variable
async def my_coroutine():
    # Get the name of the current task
    # Create a context-local variable
    task_name = asyncio.current_task().get_name()
    my_var.set(f'value_for_{task_name}')

    # Access the value of the variable in the new context
    print(f'Value in {task_name}: {my_var.get()}')

# Create a new event loop
loop = asyncio.new_event_loop()

# Run two instances of the coroutine in parallel
asyncio.set_event_loop(loop)
loop.run_until_complete(asyncio.gather(my_coroutine(), my_coroutine()))

# Close the event loop
loop.close()

print(my_var.get())