# PDGA Analysis
This is a data analysis project
[exploring](https://public.tableau.com/profile/beau5312#!/vizhome/USDiscGolfExploration/Density)
PDGA player information

## Motivation
1. I was curious to learn about the distribution of skilled disc golfers across US states
2. I had never pulled data from an API and this appeared to be a great real-world example
3. I have played around with Pandas, but primarily in academic exercises, so I wanted to use it in the wild

## How Does This Work?
1. At a high level, this code pulls player data from the PDGA API and spits out a CSV
2. There are distinct modules around [PDGA API calls](https://github.com/greenbean1/pdga-analysis/blob/main/api_calls.py),
   [dealing with CSVs](https://github.com/greenbean1/pdga-analysis/blob/main/csv_functions.py) and 
   [Pandas](https://github.com/greenbean1/pdga-analysis/blob/main/dataframes.py).
3. When running [main()](https://github.com/greenbean1/pdga-analysis/blob/main/main.py), 
   there are different options to choose from based on what is desired (ADD MORE HERE)

## Next Goal: Refactor Code
1. Type Hints: Clean up & Add for Dataframes
2. Indicate private vs public functions
3. Flush out API Calls' SessionExpired class?
4. Think about next project (Gsheets API?)

## Misc

### Project Milestones
~~1. Pull down JSON of Eagle McMahon via Requests Library~~

~~2. Save sessid & session_name into txt file so do not need to hit API for login every time~~

~~3. Save Eagle McMahon's JSON into a CSV~~

~~4. Pull down JSON and save into CSV along the way of all MPO, US players~~

~~5. Clean player API player info via CSA library~~

~~6. Get state population CSV (Census Bureau - including 54 "states)~~

~~7. Create dataframe merging CSVs with population data, number of players rated 1000+~~

~~8. Create heat map data viz (Notebook? Seaborn/Plotly/Dash/Flourish)~~

9. Refactor code (ex: truly use constants module)

### Things I Learned (or at least started learning)
1. [HTTP Status Codes](https://www.restapitutorial.com/httpstatuscodes.html)
2. [Requests Library](https://requests.readthedocs.io/en/master/)
3. [Working with JSON](https://www.geeksforgeeks.org/convert-json-to-csv-in-python/)
4. [Data Visualization Options: Tableau, Plotly, Flourish, Chartify, etc](https://spatialvision.com.au/blog-8-of-the-best-data-visualisation-platforms/)
5. [New Lines](https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/) - These primarily indicate the end of a line
6. Accessing APIs - Put in safety measures & sanity check results before scaling up (I pulled the same 200 records multiple times)
7. [Census Data is Helpful!](https://www.census.gov/newsroom/press-kits/2019/national-state-estimates.html)
8. [When reading data from CSV to Dataframe, use engine='python'](https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/)
9. [Iterating Through Dataframes](https://thispointer.com/pandas-6-different-ways-to-iterate-over-rows-in-a-dataframe-update-while-iterating-row-by-row/)
10. [Adding Columns to Dataframes Based on Criteria](https://www.dataquest.io/blog/tutorial-add-column-pandas-dataframe-based-on-if-else-condition/)
11. [Aggregations in Pandas](https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/#a-sample-dataframe)
12. [Merging Data in Pandas](https://www.tutorialspoint.com/python_pandas/python_pandas_merging_joining.htm)

### Potential Next Steps
1. For visualization: Dash, Plotly, Flourish, Chartify instead of Tableau
2. Analyze European disc golf growth (Pick top few countries -> tournament & course growth)

### Credits
Thank you [Nathan Hoover](https://github.com/nhoover) and Jan Van Bruggen for your huge help on this project!