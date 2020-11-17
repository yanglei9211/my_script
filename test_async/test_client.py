import asyncio
import requests


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8124)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

# asyncio.run(tcp_echo_client('abc'))


def test_tcp_server():
    url = 'http://127.0.0.1:9001'
    dt = {
        'x': 123,
        'y': 'abc',
        'z': [1, 'b', 3]
    }
    req = requests.post(url, dt)
    print(req.status_code)
    print(req.text)


test_tcp_server()

