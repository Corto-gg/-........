import asyncio

async def start_strongman(name, power):

    """name - имя силача
   power - подъемная мощь"""

    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i + 1} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    """Имитация соревнования"""
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3

if __name__ == '__main__':
    asyncio.run(start_tournament())

