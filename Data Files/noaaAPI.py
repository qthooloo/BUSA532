import requests
import json
import pandas as pd

# end datetime and start datetime for the data request - change these for new intervals
start_date = '2022-11-01T00:00:00'
end_date = date.today().isoformat() + 'T00:00:00'

url = f"https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-hourly&startDate={start_date}&endDate={prev_end_date}&stations=72258013960&units=standard&format=json"

response = requests.request("GET", url)
print(response.text)