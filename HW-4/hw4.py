# Question 1
# Suppose we have a SQL database that contains a table called student_info. You should run the following code block to create the database and the table.

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully");

conn.execute('''
CREATE TABLE IF NOT EXISTS student_info(first_name text,
                      last_name text,
                      credit integer,
                      gpa float);''')
print("Table created successfully");
# Clearing the table
conn.execute('DELETE FROM student_info;',);

# Inserting values
conn.execute("INSERT INTO student_info VALUES('Kate', 'Perry', 120, 3.3);")
conn.execute("INSERT INTO student_info VALUES('Kelvin', 'Harris', 50, 3.0);")
conn.execute("INSERT INTO student_info VALUES('Bin', 'Diesel', 250, 3.5);")
conn.execute("INSERT INTO student_info VALUES('nick', 'Cage', 22, 2.8);")
conn.execute("INSERT INTO student_info VALUES('Shawn', 'Carter', 100, 3.7);")
conn.execute("INSERT INTO student_info VALUES('Lucy', 'Lu', 200, 3.8 );")
conn.execute("INSERT INTO student_info VALUES('John', 'Senna', 0, 0.0 );")
conn.execute("INSERT INTO student_info VALUES('Syd', 'Barrett', 183, 2.8 );")
conn.execute("INSERT INTO student_info VALUES('Peter', 'Chao', 111, 2.3 );")
conn.execute("INSERT INTO student_info VALUES('Shang', 'abi', 64, 3.1 );")

conn.commit()
conn.close()

# This is an example of how to execute sql query

conn = sqlite3.connect('test.db')


# cursor = conn.execute(''' Your SQL Query''')


cursor = conn.execute(''' SELECT *
                          FROM student_info;''')


for row in cursor:
  print(row)
conn.close()

# Now, please write an SQL query to retrieve the first names of students whose credits are fewer than 150 and who have a GPA higher than 3.0. Then, display the results as shown in the example.

def retrieve_students():
    conn = sqlite3.connect('test.db')
    cursor = conn.execute('''
        SELECT first_name
        FROM student_info
        WHERE credit < 150 AND gpa > 3.0;
    ''')

    print("First names of students with credits < 150 and GPA > 3.0:")
    for row in cursor:
        print(row[0])

    conn.close()
    
retrieve_students()

# Question 2
# Many people in the Computer Science department use 'dot' and 'at' to replace the symbols '.' and '@' when posting their emails on websites. For example, they write 'JohndotWickatrutgersdotedu' instead of 'John.Wick@rutgers.edu.' This practice helps mitigate issues related to email scraping and spam. Suppose we have collected all the email addresses from the Computer Science department and now want to use a regular expression to extract them.

email_list = ['John[dot]Wick[at]rutgers[dot]edu',
              'Nancy@rutgers.edu.com',
              'Toby.Chavez.edu',
              'dfe.edu'
              'Steve[at]Peterson[at]rutgers[dot]edu',
              'Sydney[at]Lucas[at]rutgers[dot]edu',
              'Sydney[at][at]rutgers[dot]edu',
              'Byron.Dennis@umd.edu',
              'Nancy.Ruell@rutgers.edu',
              'Benjamin[dot]Conner[at]rutgers[dot]edu',
              'Nancy@rutgersedu',
              'dfe.edu.com',
              'dfe.edu.[]',
            ]
# Write code to read each email address and extract all valid ones. Valid email addresses are those in the formats 'first.last@domain.com', 'first.last@domain.edu', 'firstdotlastatdomaindotcom', and 'firstdotlastatdomaindotedu'. Match all valid email addresses and convert them into the format 'firstname.lastname@domain.edu' or 'firstname.lastname@domain.com'. Then, return all valid email addresses in a list.

import re

def valid_email_list(email_list):
    valid_emails = []

    for email in email_list:
        pattern = re.compile(r'([a-zA-Z]+)(\[dot\]|\.)([a-zA-Z]+)(\[at\]|@)([a-zA-Z]+)(\[dot\]|\.)(com|edu)')
        match = pattern.match(email)

        if match:
            first_name = match.group(1)
            last_name = match.group(3)
            domain = match.group(5)
            extension = match.group(7)
            valid_email = f'{first_name}.{last_name}@{domain}.{extension}'
            valid_emails.append(valid_email)

    return valid_emails
assert len(valid_email_list(email_list)) == 4
assert 'John.Wick@rutgers.edu' in valid_email_list(email_list)
assert 'Nancy.Ruell@rutgers.edu' in valid_email_list(email_list)
assert 'Benjamin.Conner@rutgers.edu' in valid_email_list(email_list)
assert 'Byron.Dennis@umd.edu' in valid_email_list(email_list)

# Problem 3: EU Cities Temperatures Dataset
# Given a CSV data file as represented by the sample file EuCitiesTemperatures.csv (213 records), load it into a Pandas DataFrame and perform the following tasks on it.

# Preprocessing/Analysis
# 1.Fill in the missing latitude and longitude values by calculating the average for that country. Round the average to 2 decimal places.

import pandas as pd

df = pd.read_csv('EuCitiesTemperatures.csv')

# Calculate the average latitude and longitude for each country
df['latitude'] = df.groupby('country')['latitude'].transform(lambda x: x.fillna(round(x.mean(), 2)))
df['longitude'] = df.groupby('country')['longitude'].transform(lambda x: x.fillna(round(x.mean(), 2)))

print(df)

# 2.Find out the subset of cities that lie between latitudes 40 to 60 (both inclusive) and longitudes 15 to 30 (both inclusive). Find out which countries have the maximum number of cities in this geographical band. (More than one country could have the maximum number of values.)

import pandas as pd

df = pd.read_csv('EuCitiesTemperatures.csv')
subset_df = df[(df['latitude'] >= 40) & (df['latitude'] <= 60) & (df['longitude'] >= 15) & (df['longitude'] <= 30)]
country_counts = subset_df['country'].value_counts()
max_count = country_counts.max()
countries_with_max_count = country_counts[country_counts == max_count].index
print("Subset of Cities:")
print(subset_df)
print("\nCountries with the Maximum Number of Cities:")
print(countries_with_max_count)


# 3.Fill in the missing temperature values by the average temperature value of the similar region type. A region type would be a combinaton of whether it is in EU (yes/no) and whether it has a coastline (yes/no).
# For example, if we have a missing temperature value for Bergen, Norway, which is not in the EU but lies on the coast, we will fill it with the average temperature of cities with EU='no' and coastline='yes'

import pandas as pd

df = pd.read_csv('EuCitiesTemperatures.csv')
def fill_missing_temperature(row):
    region_type = (row['EU'], row['coastline'])
    similar_cities = df[(df['EU'] == row['EU']) & (df['coastline'] == row['coastline']) & ~df['temperature'].isna()]
    average_temperature = similar_cities['temperature'].mean()
    return average_temperature if pd.notna(row['temperature']) else average_temperature
df['temperature'] = df.apply(fill_missing_temperature, axis=1)

print(df)

# Visualization
# For all plots, make sure to label the axes, and set appropriate tick labels.

# 1.Plot a bar chart for the number of cities belonging to each of the regions described in Preprocessing/Analysis #3 above.

import pandas as pd
import matplotlib.pyplot as plt

df['region_type'] = df['EU'] + '_' + df['coastline']
region_counts = df['region_type'].value_counts()

# Plot the bar chart
plt.figure(figsize=(10, 6))
region_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Cities in Each Region')
plt.xlabel('Region Type')
plt.ylabel('Number of Cities')
plt.xticks(rotation=45, ha='right')
plt.show()

# 2.Plot a scatter plot of latitude (y-axis) v/s longitude (x-axis) values to get a map-like visual of the cities under consideration. All the cities in the same country should have the same color.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('EuCitiesTemperatures.csv')

plt.figure(figsize=(12, 8))
for country in df['country'].unique():
    country_df = df[df['country'] == country]
    plt.scatter(country_df['longitude'], country_df['latitude'], label=country, s=80, edgecolor='w')
plt.title('Latitude vs Longitude')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Add legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.show()

# 3.The population column contains values unique to each country. So two cities of the same country will show the same population value. Plot a histogram of the number of countries belonging to each population group: split the population values into 5 bins (groups).

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('EuCitiesTemperatures.csv')

plt.figure(figsize=(10, 6))
plt.hist(df['population'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Population Groups')
plt.xlabel('Population')
plt.ylabel('Number of Countries')
plt.show()

# 4.Plot subplots (2, 2), with proper titles, one each for the region types described in Preprocessing/Analysis #3 above.

# Each subplot should be a scatter plot of Latitude (y-axis) vs. City (x-axis), where the color of the plot points should be based on the temperature values: ‘red’ for temperatures above 10, ‘blue’ for temperatures below 6 and ‘orange for temperatures between 6 and 10 (both inclusive). For each subplot, set xticks to an array of numbers from 0 to n-1 (both inclusive), where n is the total number of cities in each region type. This represents each city as a number between 0 and n-1.

import matplotlib.pyplot as plt

df['region_type'] = df['EU'] + '_' + df['coastline']
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Scatter Plots', fontsize=16)

def get_temperature_color(temp):
    if temp > 10:
        return 'red'
    elif temp < 6:
        return 'blue'
    else:
        return 'orange'
for i, region_type in enumerate(df['region_type'].unique()):
    ax = axes[i // 2, i % 2]
    region_df = df[df['region_type'] == region_type]
    colors = region_df['temperature'].apply(get_temperature_color)
    sc = ax.scatter(range(len(region_df)), region_df['latitude'], c=colors, edgecolor='w', s=80)
    ax.set_xticks(range(len(region_df)))
    ax.set_xticklabels(range(1, len(region_df) + 1))
    ax.set_title(f"Region Type: {region_type}")
    ax.set_xlabel('City')
    ax.set_ylabel('Latitude')
    legend_labels = ['> 10°C', '6 - 10°C', '< 6°C']
    ax.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in ['red', 'orange', 'blue']],
              labels=legend_labels, title='Temperature', loc='upper right')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
