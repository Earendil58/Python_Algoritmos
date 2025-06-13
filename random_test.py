import asyncio
import aiohttp
import pandas as pd

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

async def fetch_pokemon(session, id):
    url = f"{BASE_URL}{id}"
    async with session.get(url) as resp:
        return await resp.json()

async def main():
    async with aiohttp.ClientSession() as session:
        # lanzar todas las peticiones de los primeros 150
        tasks = [fetch_pokemon(session, i) for i in range(1, 151)]
        pokemons = await asyncio.gather(*tasks)

    # procesar datos
    data = []
    for p in pokemons:
        name = p["name"]
        total_stats = sum(stat["base_stat"] for stat in p["stats"])
        data.append({"name": name, "total_stats": total_stats})

    # crear DataFrame y ordenar
    df = pd.DataFrame(data)
    top5 = df.sort_values("total_stats", ascending=False).head(5)
    print("Top 5 Pokémon por suma de stats base:")
    print(top5.to_string(index=False))

if __name__ == "__main__":
    asyncio.run(main())
