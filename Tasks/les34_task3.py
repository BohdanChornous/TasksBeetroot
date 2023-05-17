import asyncio

# Task 3

HOST = '0.0.0.0'
PORT = 50000

async def process(reader, writer):
    print('Connected')
    while True:
        data = await reader.read(1024)
        if not data:
            break
        writer.write(data)
        await writer.drain()

async def main(host, port):
    server = await asyncio.start_server(process, host=host, port=port)
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main(HOST, PORT))