"""
#!/usr/bin/env python 
Short description of this Python module.

Longer description of this module.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Ben"
__authors__ = ["Ben", "etc"]
__contact__ = "ben@email.com"
__copyright__ = "Copyright 2021, $COMPANY_NAME"
__credits__ = ["Developer", "And another one", "etc"]
__date__ = "2021/07/02"
__deprecated__ = False
__email__ =  "ben@email.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Test"
__version__ = "0.0.1"

'''
Attributes
----------
aims_filepath : str
    path to .csv file used by Pandas data frame
aims_data : df
    Pandas data frame

Methods
---------    

'''

# Import Python Packages

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import scipy
import matplotlib.pyplot as plt
import seaborn as sns  # visualization

# Set Figure Size for Seaborn
sns.set(rc={'figure.figsize':(10,8)})

#print("Import Packages Complete")

# Import File and Assign to Data Frame

# Load the CSV as DataFrame using Pandas
# Must include r before path to CSV
# Path of the file to read

aims_filepath = (r"C:\Users\0016443\Corp Mail Inserter Report\data\processed\bhNavigator-AUI_Reports.csv")

# Read the file into Variable 'aims_data'
aims_data = pd.read_csv(aims_filepath, index_col='Month')

#print("Import Data Complete")

'''Understand the Data'''

# Understand the Data - Looking at the first 5 rows
aims_data.head()

# Understand the Data - Looking at the last 5 rows
aims_data.tail()

# Understand the Data - Looking at Description of Data
# Count, Mean, StdDev, Min, Max, Percentiles
aims_data.describe()

aims_data.shape

aims_data.dtypes

aims_data.columns

# Understand the Data - Number of Unique Values
# Can be used to identify Categorical vs Quantitative data
aims_data.nunique()

# Understand the Data - Unique values per column
# Change column name of column ['column name']
# Returns unique values in specified column
aims_data['Envelope Count'].unique()

'''Cleaning the Data'''

aims_data.isnull().sum()

# Removes Columns with ALL NaN values
#aims_data.dropna(axis='columns', how='all')

'''Detecting Outliers'''

# Box Plot for ALL Column in aims_data
# Need to include pyplot from matplotlib as plt
for column in aims_data.columns:
    plt.figure()
    sns.boxplot(x=aims_data[column])

'''Visualize the Data'''

# Distribution Plot for ALL Column in aims_data
for column in aims_data.columns:
    plt.figure()
    sns.displot(data=aims_data[column], kind='kde')

'''Data Relationship Analysis'''

# Relationship between Fault Count and Speed
sns.lmplot(x='Fault Count', y='Speed', data=aims_data)

# Relationship between Fault Count and Average Set Size
sns.lmplot(x='Fault Count', y='Average Set Size', data=aims_data)

# Speed has indirect correlation to Fault Count
# Average Set Size has direct correlation to Fault Count

# Relationship between Average Set Size and Machine Throughput
sns.lmplot(x='Average Set Size', y='Machine Throughput', data=aims_data)

# Machine Throughput has a direct correlation to Average Set Size

# Relationship between Average Set Size and Envelope Count
sns.lmplot(x='Average Set Size', y='Envelope Count', data=aims_data)


# Relationship between Average Set Size and Sheet Count
sns.lmplot(x='Average Set Size', y='Sheet Count', data=aims_data)

# Average Set Size has a direct correlation to Sheet Count and Envelope Count

'''Correlation Coefficient'''

# Correlation Coefficient calculation and heatmap
aims_coff = aims_data.corr()
sns.heatmap(aims_coff, annot=False)

# Pair Plot between Selected columns In aim_data
sns.pairplot(aims_data, kind='reg', diag_kind='kde', vars=['Machine Efficiency', 'Job Efficiency',
       'Envelope Count', 'Sheet Count', 'Average Set Size',
       'Speed', 'Fault Count'])