import csv
import asyncio
import aiohttp
from tqdm import tqdm


async def upload_data():
    async with aiohttp.ClientSession() as session:
        with open("data/images.csv", "r") as file:
            reader = csv.reader(file)
            for i, row in tqdm(enumerate(reader)):
                if i == 0 or row[0] == "":
                    continue

                data = list(map(int, row[1:]))
                await session.post("http://localhost:8000/upload_image", json={"data": data})

if __name__ == "__main__":
    asyncio.run(upload_data())
