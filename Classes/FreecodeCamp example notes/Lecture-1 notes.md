Notes of performing data analysis using jupyter notebooks following the [ example](../../FreeCodeCamp-Pandas-Real-Life-Example-master/Lecture_1.ipynb) provided by the instructor.
- First your import the necessary libraries. In this case we are using:- 
  - pandas for data manipulation and analysis, 
  - numpy for Python numerical computing. It provides efficient multi-dimensional array objects and various mathematical functions for handling large datasets making it a critical tool for professionals in fields that require heavy computation. numerical operations and 
  - matplotlib for data visualization.
    - %matplotlib inline to ensure that the visulization occurs after the command cell in the notebook.
- Second you load you data from the source document which range from
    - Excel files.
    - CSV files.
    - XML files.
    - Data from an API.
// sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date']    )
      explanation:- 
        This code uses the pandas library to read data from a CSV file named sales_data.csv, which is located in the data directory. The function pd.read_csv() loads the contents of the CSV file into a DataFrame, a powerful data structure for handling tabular data in Python.

        The argument parse_dates=['Date'] tells pandas to automatically interpret the values in the Date column as datetime objects rather than plain text. This is useful because it enables you to perform time-based operations (like filtering by date, resampling, or extracting month/year) more easily and accurately. Without this parameter, the Date column would be read as strings, which would require manual conversion later.

Next we view the data at a glance using the[.head()] method to view the first few rows of the data. 
  This method helps us to get an idea of the data structure, the number of rows and columns, and the date.
The [.shape] methods returns a tuple representing the dimensionality of the underlying data represented by the DataFrame object.
The [.info()] method displays information about the DataFrame, including the index dtype and column dtypes, non-nullable values, and memory usage.
The [.describe()] method generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset

