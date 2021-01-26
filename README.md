# PDGA Analysis
This is a data analysis project exploring PDGA player information

## Next Goal: Save sessid & session_name into txt file
1. Big Picture: Rewrite get_pdga_session_info()
2. Main first tries to get player stats via text file's session info - if fail then read from log in
3. Only log in if login credentials fail (save off session_name & sessid)

## Project Milestones
~~1. Pull down JSON of Eagle McMahon via Requests Library~~

~~2. Save sessid & session_name into txt file so do not need to hit API for login every time~~

~~3. Save Eagle McMahon's JSON into a CSV~~

4. Pull down JSON of all MPO, US players (test to see if inactive players get pulled)
5. Save this JSON into a CSV & put into Pandas
6. Create dataframe with state, number of players rated 1000+, state population (get this data)
7. Create heat map data viz (Notebook? Seaborn/Plotly/etc)

## Things I Learned (or at least started learning)
1. [HTTP Status Codes](https://www.restapitutorial.com/httpstatuscodes.html)
2. [Requests Library](https://requests.readthedocs.io/en/master/)
3. [Working with JSON](https://www.geeksforgeeks.org/convert-json-to-csv-in-python/)


Create new API module
Get player info for Eagle

Try
Use session info from text file
Fail
get session info from login (& set text file)

