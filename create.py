import asyncio
import csv
from twscrape import API

async def login_with_csv(api, filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip header if present
        next(reader, None)
        for row in reader:
            print(f"Row: {row}")  # Debugging statement to see the row content
            if len(row) < 4:
                continue
            email, password, username, _ = row
            await api.pool.add_account(username, password, email, password)  # Adding accounts
    await api.pool.login_all()  # Logging in all added accounts

async def main():
    api = API()
    csv_filename = 'data_udah_dicoba20.csv'  # Replace 'your_csv_file.csv' with your actual CSV file path
    await login_with_csv(api, csv_filename)

if __name__ == "__main__":
    asyncio.run(main())

