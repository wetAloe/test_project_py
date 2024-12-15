import asyncio
import csv

import aiohttp
from tqdm import tqdm
from aiohttp import ClientSession


# Function to read the CSV file and process rows asynchronously
async def upload_data(file_path):
    async with ClientSession() as session:
        # Open the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)

            tasks = []
            # Create a list to store tasks
            for i, row in tqdm(enumerate(csv_reader)):
                if i == 0 or row[0] == "":
                    continue

                data = list(map(int, row[1:]))
                tasks.append(session.post("http://localhost:8000/images/", json={"data": data}))

            # Use asyncio.gather to run all tasks concurrently
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(upload_data("data/images.csv"))
