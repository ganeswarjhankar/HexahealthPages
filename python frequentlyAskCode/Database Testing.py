import pyodbc
import pandas as pd
import matplotlib.pyplot as plt


# Set up the connection string
server = 'LAPTOP-4E931QU9'
database = 'preprod_master'
trusted_connection = 'yes'
driver = '{ODBC Driver 18 for SQL Server}'  # Driver name for Windows authentication

# Create the connection string
connection_string = f'SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};DRIVER={driver};TrustServerCertificate=yes'

#connection_string = f'SERVER={server};DATABASE={database};Trusted_Connection={trusted_connection};DRIVER={driver}'

conn = pyodbc.connect(connection_string)

cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * FROM customer")

# Fetch all rows returned by the query
rows = cursor.fetchall()



# Store the rows in a list of lists
data_list = [list(row) for row in rows]

# Convert the data_list to a pandas DataFrame for easier data manipulation and analysis
df = pd.DataFrame(data_list, columns=[column[0] for column in cursor.description])

# Perform data processing and analysis
# Example: Calculate the average age of the customers
average_age = df['id'].mean()
print("Average id:", average_age)

# Visualize the data
# Example: Plot a histogram of the ages
plt.hist(df['id'], bins=10)
plt.xlabel('id')
plt.ylabel('Count')
plt.title('Distribution of Customer Ages')
plt.show()

# Export the data to a CSV file
df.to_csv('customer_data.csv', index=False)


cursor.close()
conn.close()
