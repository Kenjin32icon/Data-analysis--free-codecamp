Data frames is similar as an excel table/spreadsheet
Easy to create data frames form csv files
The similarity of dataframe columns to series is a dataframe column would be basically a series
But for a dataframe it has multiple columns.
A 2d array is similar to a dataframe
 ## Methods
- .info() giv you quick information of the structure of you dataframe 
       - Telling you the Dtypes and non-null values
- .size you can check for the size 
- .shape
- .describe() similar to .info() you can check sumary of the structure of the data frame
           - Give you a sumarry for the statistics of the data frame 
- .dtypes gives to yhe datatypes for each column   

The .loc[] attribute will help you select individual rows
    .loc('top value': 'Last value') this method would output the selected tows that range from those values top to the last which you would want to output
    You can add a second dimention of the custom outputt you want for example
        - .loc['France':'Italy', 'Population']
The .iloc[] attributu will help you select th erow bisiquential position eg -1 = United States in the  [ data](<../../freecodecamp-intro-to-pandas-master/2 - Pandas Series exercises.ipynb>) 
        - Give me the first row last row 
  df['column'] pick a specific column you want