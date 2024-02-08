import asyncio
import os
import sys

sys.path.append("C:\\Users\\alexj\\VSCode\\Python\\Pydal")
from tidal import TidalClient


async def main():
    tidal = TidalClient(os.getenv("tidal_id"), os.getenv("tidal_secret"))
    track = await tidal.track("3146735", "GB")
    print(track["title"], " url ", track["tidalUrl"])


asyncio.run(main())