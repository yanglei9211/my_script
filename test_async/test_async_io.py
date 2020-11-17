import asyncio
import time
import functools
import concurrent.futures


async def test1():
    print(f"start tese1 at {time.strftime('%X')}")
    await asyncio.sleep(1.5)
    print("test1")
    print(f"finish tese1 at {time.strftime('%X')}")
    return "test1"


async def test2():
    print(f"start tese2 at {time.strftime('%X')}")
    await asyncio.sleep(2)
    print("test2")
    print(f"finish tese2 at {time.strftime('%X')}")
    return "test2"


async def test3():
    print(f"start tese3 at {time.strftime('%X')}")
    await asyncio.sleep(3)
    print("test3")
    print(f"finish tese3 at {time.strftime('%X')}")
    return "test3"


# def main():
#     print(f"start main at {time.strftime('%X')}")
#     loop = asyncio.get_event_loop()
#     # loop.create_task(test1())
#     # res = loop.run_until_complete(test1())
#     # loop.run_until_complete(test2())
#     r = asyncio.wait([test1(), test2(), test3()])
#     print(r, type(r))
#     res = loop.run_until_complete(r)
#     print(res, type(res))
#     s = res[0]
#     for i in s:
#         print(i, type(i))
#         print(i.done(), i.result())
#     print(f"finish main at {time.strftime('%X')}")
#
#
# main()

async def main_123():
    res = await asyncio.gather(
        test1(), test2(), test3()
    )
    print(res, type(res))

# asyncio.run(main_123())


async def fact(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: compute fact({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(2)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def main_th():
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(4))

    print(f"finished main at {time.strftime('%X')}")

# asyncio.run(main_th())


async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)


async def main_fu():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()
    fut.add_done_callback(
        functools.partial(print, "Future: ")
    )
    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(
        set_after(fut, 1, '... world'))
    # loop.run_until_complete(fut)

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(await fut)

# asyncio.run(main_fu())


def main():
    a = 0x55555555
    a = bin(a)
    print(a)
    b = bin(0x33333333)
    print(b)
    c = bin(0x0f0f0f0f)
    print(c)

main()
