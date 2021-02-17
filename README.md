# PDGA Analysis
This is a data analysis project exploring PDGA player information

## Next Goal: Refactor Code
1. Consolidate constants in constants module
2. Add link to Tableau Public viz
3. Add Motivation, How Does This Work, Potential Next Steps & Credits 
4. Code Review with Dad -> how to better organize within modules?

## Project Milestones
~~1. Pull down JSON of Eagle McMahon via Requests Library~~

~~2. Save sessid & session_name into txt file so do not need to hit API for login every time~~

~~3. Save Eagle McMahon's JSON into a CSV~~

~~4. Pull down JSON and save into CSV along the way of all MPO, US players~~

~~5. Clean player API player info via CSA library~~

~~6. Get state population CSV (Census Bureau - including 54 "states)~~

~~7. Create dataframe merging CSVs with population data, number of players rated 1000+~~

~~8. Create heat map data viz (Notebook? Seaborn/Plotly/Dash/Flourish)~~

9. Refactor code (ex: truly use constants module)

## Things I Learned (or at least started learning)
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

## Potential Next Steps
1. For visualization: Dash, Plotly, Flourish, Chartify instead of Tableau
2. Analyze European disc golf growth (Pick top few countries -> tournament & course growth)