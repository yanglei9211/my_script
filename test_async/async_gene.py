#!/usr/bin/env python
# encoding: utf-8

from time import sleep
import asyncio
import random


class P:
    @classmethod
    def make(cls, num, *args, **kwargs):
        ps = []
        for i in range(num):
            ps.append(cls.__new__(cls, *args, **kwargs))
        return ps


all_ps = P.make(5)
# for i in all_ps:
#     print(i)


async def ask_for_p():
    s = random.random()
    t = random.randint(1, 10)
    await asyncio.sleep(s)
    print("make new: %d ps cost: %fs" % (t, s))
    all_ps.extend(P.make(t))


async def take_p(num):
    cnt = 0
    while True:
        if len(all_ps) == 0:
            print("wait new p")
            # sleep(.1)
            await ask_for_p()
        else:
            p = all_ps.pop()
            yield p
            cnt += 1
            if cnt == num:
                break


async def buy_p():
    bk = []
    async for p in take_p(50):

        bk.append(p)
        print(f'Got p {id(p)}')
    # return bk
    print("done")
    print(len(all_ps))

# r = buy_p()
# print(r)


def main():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(buy_p())
    asyncio.wait()
    loop.close()


main()
