import asyncio
import time


async def fetch_data(seconds):
    print("Начинаем запрос 1")
    await asyncio.sleep(seconds)
    print("Заканчиваем запрос 1")


async def fetch_data_2(seconds):
    print("Начинаем запрос 2")
    await asyncio.sleep(seconds)
    print("Заканчиваем запрос 2")


async def main():
    start= time.time()

    await asyncio.gather(fetch_data(4), fetch_data_2(2))

    end = time.time()
    print(f"Общее выполненние функии {end - start}")

asyncio.run(main())
#end at FastAPI 4:00:00