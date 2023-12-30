# EmployeeStatistics
Employee Data Analysis Script

This Python script is designed for comprehensive analysis of employee data, typically stored in an Excel file. It uses the pandas and matplotlib libraries to read data, calculate various statistics, and visualize the results. This script is ideal for HR departments, business analysts, and data scientists who need to analyze and present employee-related data.

Key Features
Data Reading: Reads employee data from an Excel file, specifically from the 'Sheet1' sheet.

Total Employee Count: Calculates and displays the total number of employees in the dataset.
Department Analysis: Calculates the total number of employees in each department.
Visualizes this data in a bar chart with a custom color palette.

Country Distribution:
Calculates the percentage of employees in each country.
Displays this information in a pie chart, highlighting the country with the largest percentage.

Job Title Analysis:
Counts the number of employees in each job title.
Displays this data in a table format.

Salary Analysis:
Calculates the total sum of employees' salaries in each business unit.
Presents this data in a table format, with salaries formatted as float values.

Age Demographics:
Segments employees into age ranges and calculates the percentage in each range.
Visualizes these percentages in a bar chart.

Usage
Input: The script expects an Excel file named 'Employeedata.xlsx', containing employee data with columns such as 'Department', 'Country', 'Job Title', 'Annual Salary', and 'Age'.
Output: The script outputs a series of charts and tables that provide insights into the composition and distribution of employees.

Requirements
To run this script, the following Python libraries are required:
pandas: For data manipulation and analysis.
matplotlib: For creating static, interactive, and animated visualizations.
