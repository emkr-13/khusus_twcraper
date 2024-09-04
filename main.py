import asyncio
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()
    # ADD ACCOUNTS (for CLI usage see BELOW)
    # await api.pool.add_account("WahyudiMil23368", "icaimutt", "cevogemozon@idemainc.com", "icaimutt")
    await api.pool.login_all()

if __name__ == "__main__":
    asyncio.run(main())