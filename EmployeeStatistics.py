import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the Excel file
data = pd.read_excel('/Users/divya/Downloads/Employeedata.xlsx', sheet_name='Sheet1')

# Get the total number of employees (number of rows in the DataFrame)
total_employees = len(data)

# Display the total number of employees
print(f'Total Number of Employees: {total_employees}')

# Get the Total Number of Employees in each department
department_counts = data['Department'].value_counts()

# Define a color palette for the bars
colors = ['skyblue', 'lightcoral', 'lightsteelblue', 'lightsalmon',
'lightseagreen', 'palevioletred', 'cornflowerblue', 'lightgoldenrodyellow', 'mediumaquamarine']

# Plot the Total Number of Employees in each department in a Bar Chart
department_counts.plot(kind='bar', rot=0, color=colors)
plt.title('Total Number of Employees in Each Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.show()

# Display the Percentage of Employees in each Country in Pie Chart
country_percentage = data['Country'].value_counts(normalize=True) * 100
explode_values = tuple([0.1] + [0] * (len(country_percentage) - 1))  # Highlight the first slice
country_percentage.plot(kind='pie', autopct='%1.1f%%', startangle=90, explode=explode_values, shadow=True)
plt.title('Percentage of Employees in Each Country')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Display the Total number of Employees in Each Job Titles in Table format
job_title_counts = data['Job Title'].value_counts()
job_title_table = pd.DataFrame(job_title_counts)
job_title_table.columns = ['Total Employees']
print('\nTotal number of Employees in Each Job Title:')
print(job_title_table)

# Display the Total Sum of Employees Salaries in Each Business Unit in Table Format
data['Annual Salary'] = data['Annual Salary'].replace('[\$,]', '', regex=True).astype(float)
salary_by_business_unit = data.groupby('Business Unit')['Annual Salary'].sum()
salary_by_business_unit_table = pd.DataFrame(salary_by_business_unit)
salary_by_business_unit_table.columns = ['Total Salary']
print('\nTotal Sum of Employees Salaries in Each Business Unit:')
print(salary_by_business_unit_table)

# Specify the age bins
bins = [20, 30, 40, 50, 60, 70, 80]

# Create age ranges and calculate the percentage
age_ranges = pd.cut(data['Age'], bins=bins, right=False)
age_percentage = age_ranges.value_counts(normalize=True) * 100

# Define a color palette for the bars
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightsteelblue', 'lightsalmon']

# Plot the Percentage of Employees in Each Age Range in a Bar Chart
age_percentage.sort_index().plot(kind='bar', color=colors, width=0.8)
plt.title('Percentage of Employees in Each Age Range')
plt.xlabel('Age Range')
plt.ylabel('Percentage')
plt.show()
