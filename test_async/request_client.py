import requests
import time
from hyper.contrib import HTTP20Adapter, HTTPAdapter
from pprint import pprint


def test_1():
    t1 = time.time() * 1000
    # url = "https://www.baidu.com"
    url = "https://gemserver.test.17zuoye.net"
    session = requests.session()
    session.mount(url, HTTPAdapter())
    r = session.get(url)
    t2 = time.time() * 1000
    print(t2 - t1)
    print(r)
    # print(r.text)
    return t2-t1


def test_2():
    t1 = time.time() * 1000
    url = "https://gemserver.test.17zuoye.net"
    session = requests.session()
    session.mount(url, HTTP20Adapter())
    r = session.get(url)
    t2 = time.time() * 1000
    print(t2 - t1)
    print(r)
    # print(r.text)
    return t2-t1


def test_12():
    tot = 20
    t1 = 0.0
    for i in range(tot):
        t1 += test_1()
    t1 = t1 / tot

    t2 = 0.0
    for i in range(tot):
        t2 += test_2()
    t2 = t2 / tot
    print(t1)
    print(t2)



def main():
    url = "http://127.0.0.1:9001/x"
    # session = requests.session()
    # req = session.post(url, {'x': 1, 'y': 2, 'z': 3})
    req = requests.post(url, {'x':1, 'y':2, 'z': 3})
    # req = session.post(url)
    print(req.status_code)
    print(req.text)


if __name__ == '__main__':
    # test_12()
    main()
