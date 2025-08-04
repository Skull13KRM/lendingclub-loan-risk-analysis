# -*- coding: utf-8 -*-
"""
Created on Mon 4 Aug 2025

@author: KeeganMurphy
"""

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =============================================================================
# Loading data
# =============================================================================

# Importing datasets
loan_data = pd.read_excel('loandataset.xlsx')
customer_data = pd.read_csv('customer_data.csv', sep=';')

# Display the first few rows of the dataset
print(loan_data.head())
print(customer_data.head())

# Merging two dataframes on id
complete_data = pd.merge(loan_data, customer_data, left_on='customerid', right_on='id')

# =============================================================================
# Cleaning Data
# =============================================================================

# Check for missing data
complete_data.isnull().sum()

# Remove the rows with missing data
complete_data = complete_data.dropna()
complete_data.isnull().sum()

# Check for duplicated data
complete_data.duplicated().sum()

# Dropping duplicates
complete_data = complete_data.drop_duplicates()
complete_data.duplicated().sum()

# =============================================================================
# Functions in Python
# =============================================================================

# def function_name(parameter1, parameter2):
#     #operation that needs to be done
#     return result

def add_numbers(number1, number2):
    sum = number1 + number2
    return sum

result = add_numbers(10, 15)
print(result)

# Creating a conditional statement function
def check_number(number):
    if number > 0:
        return 'Positive'
    elif number < 0:
        return 'Negative'
    else:
        return 'Zero'

# Test/Check
result = check_number(0)
print(result)

# =============================================================================
# Creating new features
# =============================================================================

# define a function to categorize purpose into broader categories
def categorize_purpose(purpose):
    if purpose in ['credit_card', 'debt_consolidation']:
        return 'Financial'
    elif purpose in ['education', 'small_business']:
        return 'Educational/Business'
    else:
        return 'Other'

# Test/Check
categorize_purpose('credit_card')

# Applyig the function to the dataset
complete_data['purpose_category'] = complete_data['purpose'].apply(categorize_purpose)


# Create a new function: 
#   If the dti ratio is more than 20 
#   and the delinq.2years is greater than 2
#   and the revol.util is greater than 60
# then the borrower is high risk

def assess_risk(row):
    if row['dti'] > 20 and row['delinq.2yrs'] > 2 and row['revol.util'] > 60:
        return 'High Risk'
    else:
        return 'Low Risk'

# Applyig the function to the complete_data dataframe
complete_data['Risk'] = complete_data.apply(assess_risk, axis=1)


# Create a new function:
# Categorizing fico scores

def categorize_fico(fico_score):
    if fico_score >= 800 and fico_score <= 850:
        return 'Excellent'
    elif fico_score >= 740 and fico_score <800:
        return 'Very Good'
    elif fico_score >= 670 and fico_score <740:
        return 'Good'
    elif fico_score >=580 and fico_score <670:
        return 'Fair'
    else:
        return 'Poor'

# Applyig the function to the complete_data dataframe
complete_data['fico_category'] = complete_data['fico'].apply(categorize_fico)


# Create a new function:
# Identify customers with more than average inquiries and derogatory records

def identify_high_inq_derog(row):
    
    average_inq = complete_data['inq.last.6mths'].mean()
    average_derog = complete_data['pub.rec'].mean()
    
    if row['inq.last.6mths'] > average_inq and row['pub.rec'] > average_derog:
        return True
    else:
        return False

# Applyig the function to the complete_data dataframe
complete_data['high_inq_and_derog'] = complete_data.apply(identify_high_inq_derog, axis=1)

# =============================================================================
# Classes in Python
# =============================================================================

# Creating a data analysis class to calculate summary statistics
class DataAnalysis:
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
        
    def calculate_mean(self):
        return self.df[self.column_name].mean()
    
    def calculate_median(self):
        return self.df[self.column_name].median()

analysis = DataAnalysis(complete_data, 'fico')
mean_fico = analysis.calculate_mean()
median_fico = analysis.calculate_median()

# =============================================================================
# Data Visualizations
# =============================================================================

# Set the style of our visualizations (darkdrid, whitegrid, dark, white)
sns.set_style('darkgrid')

# Bar plot to show distribution of loans by purpose
# Seaborn palette = 'deep', 'pastel', 'dark', 'muted', 'bright, 'colorblind'
plt.figure(figsize=(10,6))
sns.countplot(x= 'purpose', data= complete_data, palette= 'dark')
plt.title('Loan Purpose Distribution')
plt.xlabel('Purpose of loan')
plt.ylabel('Number of Loans')
plt.xticks(rotation=45)
plt.show()

# Create a scatter plot for 'dti' vs 'income
plt.figure(figsize=(10,6))
sns.scatterplot(x= 'log.annual.inc', y= 'dti', data= complete_data)
plt.title('Debt-to-Income Ratio vs Annaul Income')
plt.show()

# Distribution of FICO scores
plt.figure(figsize=(10,6))
sns.histplot(complete_data['fico'], bins=30, kde= True)
plt.title('Distribution of FICO scores')
plt.show()

# Box plot - Risk Category vs Interest Rate
plt.figure(figsize=(10,6))
sns.boxenplot(x= 'Risk', y= 'int.rate', data= complete_data)
plt.title('Risk Category vs Interest Rate')
plt.show()


# Subplots

# Initialize the subplot figure
fig, axs = plt.subplots(2, 2, figsize=(20, 20))

# 1. Loan Purpose Distribution
sns.countplot(x= 'purpose', data= complete_data, ax= axs[0, 0])
axs[0, 0].set_title('Loan Purpose Distribution')
plt.setp(axs[0, 0].xaxis.get_majorticklabels(), rotation=45)

# 2. Debt-to-Income Ratio vs Annaul Income
sns.scatterplot(x= 'log.annual.inc', y= 'dti', data= complete_data, ax= axs[0, 1])
axs[0, 1].set_title('Debt-to-Income Ratio vs Annaul Income')

# 3. Distribution of FICO scores
sns.histplot(complete_data['fico'], bins=30, kde= True, ax= axs[1, 0])
axs[1, 0].set_title('Distribution of FICO scores')

# 4. Risk Category vs Interest Rate
sns.boxenplot(x= 'Risk', y= 'int.rate', data= complete_data, ax= axs[1, 1])
axs[1, 1].set_title('Risk Category vs Interest Rate')


# Adjust layout for readability
plt.tight_layout()
plt.show()


















