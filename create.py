import asyncio
import csv
from twscrape import API

async def login_with_csv(api, filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header if present
        next(reader, None)
        for row in reader:
            email, password, username, _ = row  # Assuming the CSV format is email,password,username,password
            await api.pool.add_account(username, password, email, password)  # Adding accounts
    await api.pool.login_all()  # Logging in all added accounts

async def main():
    api = API()
    csv_filename = 'data_udah_dicoba11.csv'  # Replace 'your_csv_file.csv' with your actual CSV file path
    await login_with_csv(api, csv_filename)

if __name__ == "__main__":
    asyncio.run(main())
