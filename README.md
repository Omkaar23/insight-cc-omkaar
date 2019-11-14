# insight-cc-omkaar
The challenge follows the following steps: 

<b> 1. Converting data to nested dictionary format: </b>  

CSV files are first converted into the form of nested dictionary. 
For example, for a sample input file, the corresponding dictionary structure is shown below: 

`{('US-Canada Border', 'Truck Containers Full'): {'03/01/2019 12:00:00 AM': [6483]},
}`

<b> 2. Calculating the sum of every crossing measure for each month </b>  

<b> 3. Calculating running monthly average of total crossings: </b>

In the above-mentioned dictionary structure, for each measure and for each date we have corresponding total count of passengers who passed the border which is represented in the form of list of lists. 
- If the length of list is 1, we have running monthly average of 0. 
- For value greater than 1, we'll add the value of crossings for previous months and divide the answer by count of previous months to get the running average of current item. 

<b> 4. Converting the dictionary into a list format and sorting to the appropriate output format  </b>

The nested dictionary structure is converted to a list of lists and further sorted to matchthe output format of report.csv
