# FreeCodeCamp Pandas Real-Life Example Course

Welcome to the **FreeCodeCamp Pandas Real-Life Example Course**!  
By Lewis Kariuki, forked and adapted from FreeCodeCamp's Data Analysis with Python course.

This project helps you learn the fundamentals of data analysis with Python. By the end, you'll know how to read data from sources like CSVs and SQL, and use open-source libraries such as Numpy, Pandas, Matplotlib, and Seaborn to process and visualize data.

The course provides hands-on exercises using Python and Pandas, focusing on real-world datasets from retail and DVD rental domains.

---

## Project Structure

```
├── Classes/
│   ├── 1. Introduction to Data Analysis
│   │        └──notes.md
│   ├── 2. Data Analysis Example A
│   │        └──notes.md
│   ├── 3. Data Analysis Example B
│   │        └──notes.md
│   ├── 4. How to use Jupyter Notebooks Intro
│   │       ├──test.ipynb
│   │        └──notes.md
│   ├── 5. Jupyter Notebooks Cells
│   ├── 6. Jupyter Notebooks Importing and Exporting Data/
│   │   ├── yfinance training/
│   │   │   ├── yfinance_script.py
│   │   │   ├── my yfinance notes.md
│   │   │   ├── yfinance-test.ipynb
│   │   │   ├── AAPL_historical_data.csv// test result data from the yfinance-test.ipynb
│   │   │   ├── notes.md
│   │   │   └── yfinance notes from geeksforgeeks.md
│   │   └── ...other notebooks and scripts...
│   ├── 7. Numpy Introduction A
│   │        └──notes.md
│   ├── 8. Numpy Introduction  b
│   │        ├──notes.md
│   │        └──numpy-test.ipynb
│   ├── 9. Numpy Arrays
│   │        ├──notes.md
│   │        └──numpy-arrays.ipynb
│   ├── 10. Numpy Operations
│   │        └──notes.md
│   ├── NumPY.ipynb
│   └── FreecodeCamp example notes
FreeCodeCamp-Pandas-Real-Life-Example-master/
│
├── Exercises_1.ipynb      # Bike store sales analysis exercises
├── Exercises_2.ipynb      # Sakila DVD rental database exercises
├── Lecture_1.ipynb        # Guided bike store sales analysis
├── Lecture_2.ipynb        # Guided Sakila database analysis
├── data/
│   ├── chinook.db         # Chinook sample database (SQLite)
│   ├── sakila.db          # Sakila sample database (SQLite)
│   └── sales_data.csv     # Bike store sales data (CSV)

└── README.md              # Course and project overview
```

---

## Datasets

- **sales_data.csv**: Bike store sales data, including customer demographics, product categories, and transaction details.
- **sakila.db**: Sakila DVD rental database, modeling a rental store (films, actors, rentals, etc.).
- **chinook.db**: Chinook music store database (optional, for advanced exercises).

---

## Classes Directory

The `Classes/` folder contains additional learning resources and practical notebooks, including:

- **Jupyter Notebooks Importing and Exporting Data**:  
  - Practice with importing/exporting data in various formats.
  - Includes a `yfinance training` subfolder with scripts and notes for fetching and analyzing financial data from Yahoo Finance using the `yfinance` Python library.
  - Example:  
    - `yfinance_script.py`: Script to fetch financial data.
    - `my yfinance notes.md`: Notes and sample outputs from running the script.
    - `yfinance notes from geeksforgeeks.md`: Reference notes from GeeksforGeeks.

Explore these materials for hands-on experience with real-world data sources and APIs.

---

## What You'll Learn

- Loading and exploring datasets with Pandas
- Data cleaning, wrangling, and transformation
- Statistical analysis and summary statistics
- Data visualization with Matplotlib and Seaborn (histograms, box plots, scatter plots, pie charts, KDE)
- Grouping, aggregation, and pivot tables
- Working with SQL databases in Python
- Fetching and analyzing financial data with `yfinance`
- Real-world business insights from sales and rental data

---

## Getting Started

1. **Install requirements**:  
   - Python 3.x  
   - Jupyter Notebook or JupyterLab  
   - pandas, matplotlib, numpy, seaborn, sqlite3, yfinance

2. **Open the notebooks**:  
   - Start with `Lecture_1.ipynb` and `Lecture_2.ipynb` for guided walkthroughs.
   - Try `Exercises_1.ipynb` and `Exercises_2.ipynb` for hands-on practice.
   - Explore the `Classes/` directory for additional examples and scripts.

3. **Explore the data**:  
   - Use the datasets in the `data/` folder and try fetching new data with `yfinance`.

---

## Course Authors

- [rmotr.com](https://rmotr.com/data-science-python-course)
- Adapted for FreeCodeCamp by Lewis Kariuki

---

## License

This material is for educational purposes only.

---

Happy analyzing!
# FreeCodeCamp Pandas Real-Life Example Course

Welcome to the **FreeCodeCamp Pandas Real-Life Example Course**!  
By Lewis Kariuki, forked and adapted from FreeCodeCamp's Data Analysis with Python course.

This project helps you learn the fundamentals of data analysis with Python. By the end, you'll know how to read data from sources like CSVs and SQL, and use open-source libraries such as Numpy, Pandas, Matplotlib, and Seaborn to process and visualize data.

The course provides hands-on exercises using Python and Pandas, focusing on real-world datasets from retail and DVD rental domains.

---

## Project Structure

```
├── Classes/
│   ├── 1. Introduction to Data Analysis
│   │        └──notes.md
│   ├── 2. Data Analysis Example A
│   │        └──notes.md
│   ├── 3. Data Analysis Example B
│   │        └──notes.md
│   ├── 4. How to use Jupyter Notebooks Intro
│   │       ├──test.ipynb
│   │        └──notes.md
│   ├── 5. Jupyter Notebooks Cells
│   ├── 6. Jupyter Notebooks Importing and Exporting Data/
│   │   ├── yfinance training/
│   │   │   ├── yfinance_script.py
│   │   │   ├── my yfinance notes.md
│   │   │   ├── yfinance-test.ipynb
│   │   │   ├── AAPL_historical_data.csv// test result data from the yfinance-test.ipynb
│   │   │   ├── notes.md
│   │   │   └── yfinance notes from geeksforgeeks.md
│   │   └── ...other notebooks and scripts...
│   ├── 7. Numpy Introduction A
│   │        └──notes.md
│   ├── 8. Numpy Introduction  b
│   │        ├──notes.md
│   │        └──numpy-test.ipynb
│   ├── 8. Numpy Arrays
│   │        ├──notes.md
│   │        └──numpy-arrays.ipynb
│   └── FreecodeCamp example notes
FreeCodeCamp-Pandas-Real-Life-Example-master/
│
├── Exercises_1.ipynb      # Bike store sales analysis exercises
├── Exercises_2.ipynb      # Sakila DVD rental database exercises
├── Lecture_1.ipynb        # Guided bike store sales analysis
├── Lecture_2.ipynb        # Guided Sakila database analysis
├── data/
│   ├── chinook.db         # Chinook sample database (SQLite)
│   ├── sakila.db          # Sakila sample database (SQLite)
│   └── sales_data.csv     # Bike store sales data (CSV)

└── README.md              # Course and project overview
```

---

## Datasets

- **sales_data.csv**: Bike store sales data, including customer demographics, product categories, and transaction details.
- **sakila.db**: Sakila DVD rental database, modeling a rental store (films, actors, rentals, etc.).
- **chinook.db**: Chinook music store database (optional, for advanced exercises).

---

## Classes Directory

The `Classes/` folder contains additional learning resources and practical notebooks, including:

- **Jupyter Notebooks Importing and Exporting Data**:  
  - Practice with importing/exporting data in various formats.
  - Includes a `yfinance training` subfolder with scripts and notes for fetching and analyzing financial data from Yahoo Finance using the `yfinance` Python library.
  - Example:  
    - `yfinance_script.py`: Script to fetch financial data.
    - `my yfinance notes.md`: Notes and sample outputs from running the script.
    - `yfinance notes from geeksforgeeks.md`: Reference notes from GeeksforGeeks.

Explore these materials for hands-on experience with real-world data sources and APIs.

---

## What You'll Learn

- Loading and exploring datasets with Pandas
- Data cleaning, wrangling, and transformation
- Statistical analysis and summary statistics
- Data visualization with Matplotlib and Seaborn (histograms, box plots, scatter plots, pie charts, KDE)
- Grouping, aggregation, and pivot tables
- Working with SQL databases in Python
- Fetching and analyzing financial data with `yfinance`
- Real-world business insights from sales and rental data

---

## Getting Started

1. **Install requirements**:  
   - Python 3.x  
   - Jupyter Notebook or JupyterLab  
   - pandas, matplotlib, numpy, seaborn, sqlite3, yfinance

2. **Open the notebooks**:  
   - Start with `Lecture_1.ipynb` and `Lecture_2.ipynb` for guided walkthroughs.
   - Try `Exercises_1.ipynb` and `Exercises_2.ipynb` for hands-on practice.
   - Explore the `Classes/` directory for additional examples and scripts.

3. **Explore the data**:  
   - Use the datasets in the `data/` folder and try fetching new data with `yfinance`.

---

## Course Authors

- [rmotr.com](https://rmotr.com/data-science-python-course)
- Adapted for FreeCodeCamp by Lewis Kariuki

---

## License

This material is for educational purposes only.

---

Happy analyzing!