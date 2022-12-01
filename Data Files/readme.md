## What I have so far

I have included the first data file I found just in case (`DailyGHCN_2020_to_20201125.csv`) and its associated documentation file. I don't think we will end up using this though because it's a daily file.

Also included is a python script `noaaAPI.py` for fetching an hourly file for DFW airport. I think this will be our best bet. I had to stop for now so I didn't get farther than bringing back the response. This should be a great starting point, though!

Website for searching through the various datasets available for our area

https://www.ncei.noaa.gov/access/search/dataset-search?bbox=32.926,-97.067,32.866,-97.007

Note: Once you select a dataset, the URL will give you pretty much everything you need to build the HTTP request.

Here is the best documentation I was able to find for the API: https://www.ncei.noaa.gov/support/access-data-service-api-user-documentation