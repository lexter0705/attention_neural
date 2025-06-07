import abc
import asyncio

from websockets import ConnectionClosed, connect, ClientConnection


class WebsocketConnector(abc.ABC):
    def __init__(self, link: str):
        self.__link = link
        self.__websocket: ClientConnection | None = None

    async def connect(self) -> None:
        async with connect(self.__link) as websocket:
            self.__websocket = websocket
            await self.on_start()
            async for message in websocket:
                try:
                    await self.on_message(message)
                except ConnectionClosed:
                    await self.on_close()
                await asyncio.sleep(1)

    async def on_start(self) -> dict:
        pass

    async def on_close(self):
        pass

    async def on_message(self, message: str):
        pass

    @property
    def link(self) -> str:
        return self.__link

    @property
    def websocket(self) -> ClientConnection:
        if self.__websocket is None:
            raise Exception('Websocket not connected')
        return self.__websocket