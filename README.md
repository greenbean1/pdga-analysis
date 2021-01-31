# PDGA Analysis
This is a data analysis project exploring PDGA player information

## Next Goal: Get lots of player info (hella JSON)
1. Use API query's limit, offset, division_code, country parameters
2. Get 200 players with each query, offset by 1 then continue
3. How to save these 200 players? Append to a dataframe?

## Project Milestones
~~1. Pull down JSON of Eagle McMahon via Requests Library~~

~~2. Save sessid & session_name into txt file so do not need to hit API for login every time~~

~~3. Save Eagle McMahon's JSON into a CSV~~

4. Pull down JSON and save into CSV along the way of all MPO, US players
6. Get state population CSV (Census Bureau)
7. Create dataframe merging CSVs with population data, number of players rated 1000+
8. Create heat map data viz (Notebook? Seaborn/Plotly/Dash/Flourish)

## Things I Learned (or at least started learning) - add to JSON part (data format in general, JSON vs dictionaries & converting to CSV)
1. [HTTP Status Codes](https://www.restapitutorial.com/httpstatuscodes.html)
2. [Requests Library](https://requests.readthedocs.io/en/master/)
3. [Working with JSON](https://www.geeksforgeeks.org/convert-json-to-csv-in-python/)
4. [Flourish](https://flourish.studio/visualisations/maps/?utm_source=showcase&utm_campaign=visualisation/4424060)
5. [New Lines](https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/) - These primarily indicate the end of a line