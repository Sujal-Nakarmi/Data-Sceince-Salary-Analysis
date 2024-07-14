#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd #importing pandas and assigning into alias 
import matplotlib.pyplot as plt #importing pandas and assigning into alias 


# # Data Preparation

# ## Question 1

# ### Write a python program to load data into pandas DataFrame

# In[2]:


data = pd.read_csv('DataScienceSalaries_.csv') 


#read.csv() is a function of dataframe to import DataScienceSalaries.csv and convert into DataFrame and storing in data variable'''


# In[3]:


data.head() #printing by using head function to display the first 5 rows to check if the file is being imported or not


# ### Replacing all Data which are inconsistent

# In[4]:


data['job_title'].replace({'Principal Data Scientist':'Data Scientist',
                           'Product Data Scientist':'Data Scientist',
                           'Staff Data Scientist':'Data Scientist',
                           'Applied Data Scientist':'Data Scientist',
                           'Data Scientist Lead':'Data Scientist',
                           'Lead Data Scientist':'Data Scientist'} ,inplace = True)

#In column job_title replacing data which are inconsistent. This is the code for replacing all heading 
#using replace function relating to data scientist and replacing them as Data Scientist


# In[5]:


data['job_title'].replace({'ML Engineer':'Machine Learning ',
                           'Applied Machine Learning Engineer':'Machine Learning ',
                           'Machine Learning Engineer' : 'Machine Learning ',
                           'Machine Learning Researcher':'Machine Learning ',
                           'Machine Learning Scientist':'Machine Learning ',
                           'Machine Learning Infrastructure Engineer':'Machine Learning ',
                           'Head of Machine Learning':'Machine Learning ',
                           'Applied Machine Learning Scientist':'Machine Learning ',
                           'Machine Learning Manager': 'Machine Learning ',
                           'Lead Machine Learning Engineer': 'Machine Learning ',
                           'Principal Machine Learning Engineer': 'Machine Learning ',
                           'Machine Learning Research Engineer': 'Machine Learning ',
                           'Machine Learning Software Engineer': 'Machine Learning ',
                           'Machine Learning Developer':'Machine Learning '} ,inplace = True)

#In column job_title replacing data which are inconsistent. This is the code for replacing all heading using
#replace function relating to Machine Learning and replacing them as Machine Learning


# In[6]:


data['job_title'].replace({ 
                            'Lead Data Analyst':'Data Analyst',
                            'Financial Data Analyst':'Data Analyst',
                            'Product Data Analyst':'Data Analyst',
                            'Marketing Data Analyst':'Data Analyst',
                            'Principal Data Analyst':'Data Analyst',
                            'Finance Data Analyst':'Data Analyst',
                            'Data Quality Analyst':'Data Analyst',
                            'Compliance Data Analyst':'Data Analyst',
                            'Business Data Analyst':'Data Analyst',
                            'Staff Data Analyst':'Data Analyst',
                            'BI Data Analyst':'Data Analyst'} ,inplace = True)

#In column job_title replacing data which are inconsistent. This is the code for replacing all heading using replace 
#function relating to Data Analyst and replacing them as Data Analyst


# In[7]:


data['job_title'].replace({ 
                            
                            'Big Data Engineer':'Data Engineer',
                            'Software Data Engineer':'Data Engineer',
                            'Cloud Data Engineer':'Data Engineer',
                            'Azure Data Engineer':'Data Engineer',
                            'Marketing Data Engineer':'Data Engineer',
                            'Lead Data Engineer':'Data Engineer',
                            'BI Data Engineer':'Data Engineer',
                            'Principal Data Engineer':'Data Engineer'} ,inplace = True)


#In column job_title replacing data which are inconsistent. This is the code for replacing all heading 
#using replace function relating to Data Engineer and replacing them as Data Engineer'''


# In[8]:


data['job_title'].replace({ 
                            'Big Data Architect':'Data Architect',
                            'Principal Data Architect':'Data Architect',
                            'Cloud Data Architect':'Data Architect' } ,inplace = True)


#In column job_title replacing data which are inconsistent. This is the code for replacing all heading 
#using replace function relating to Data Architect and replacing them as Data Architect'''


# In[9]:


data['job_title'].replace ({'Data Analytics Manager':'Data Analytics',
                            'Data Analytics Engineer':'Data Analytics',
                            'Data Analytics Consultant':'Data Analytics',
                            'Data Analytics Specialist':'Data Analytics',
                            'Data Analytics Lead':'Data Analytics',} ,inplace= True)
                            
#In column job_title replacing data which are inconsistent. This is the code for replacing all heading 
#using replace function relating to Data Analytics and replacing them as Data Analytics


# In[10]:


data['job_title'].replace({'Data Science Manager':'Data Science',
'Director of Data Science':'Data Science',
'Data Science Lead':'Data Science',
'Data Science Consultant':'Data Science',
'Head of Data Science':'Data Science',
'Data Science Engineer':'Data Science',
'Data Science Tech Lead':'Data Science'},inplace= True)

#In column job_title replacing data which are inconsistent. This is the code for replacing all heading 
#using replace function relating to Data Science and replacing them as Data Science


# ## Question 2

# ### Write a python program to remove unnecessary columns i.e., salary and salary currency.

# In[11]:


data.drop(['salary','salary_currency'], axis = 1, inplace = True) # axis =1 determines column, 
                                                #inplace = True for change permanently in original data set


# In[12]:


data # printing to see the change in DataFrame


# ## Question 3

# ### Write a python program to remove the NaN missing values from updated dataframe

# In[13]:


data.isnull() #Checking the null value is present or not using isnull function


# In[14]:


data.isnull().sum() #Checking null value count in each column by adding sum function


# In[15]:


data.dropna() #dropping NaN value using dropna function from the DataFrame
data


# ## Question 4

# ### Write a python program to check duplicates value in the dataframe.

# In[16]:


data.duplicated() # Checking duplicate value using duplicated function


# In[17]:


data.duplicated().sum() #Displaying total number of rows which are duplicated in DataFrame


# In[18]:


data.loc[data.duplicated(), :] # Retreving only duplicated rows from all the column


# In[19]:


data.drop_duplicates(keep="first",inplace=True) #Deleting all the duplicated value and keeping the first occurence
data


# ## Question 5

# ### Write a python program to see the unique values from all the columns in the dataframe.

# In[21]:


for column in data: #using for each loop in the column of dataframe to iterate over each column
    print("Unique Value in", column + ':') #printing to know which column value is being printed
    print (data[column].unique()) #retreiving unique values from column 


# ## Question 6

# ### Rename the experience level columns as below.

# ### SE – Senior Level/Expert MI – Medium Level/Intermediate EN – Entry Level EX – Executive Level

# In[22]:


data['experience_level'].replace({'SE': 'Senior level/Expert', #Replacing SE with Senior level/Expert
                                  'EN': 'Entry Level',  #Replacing EN with Entry level
                                  'MI': 'Medium Level/Intermediate', #Replacing MI with Medium level/Intermediate
                                  'EX':'Executive Level'}, inplace = True) #Replacing EX with Executive level


data # printing to check if there is any change or not


# # Data Analysis

# ## Question 1

# ### Write a Python program to show summary statistics of sum, mean, standard deviation, skewness, and kurtosis of any chosen variable. 

# In[23]:


data.describe() #showing summary stats of DataFrame


# In[25]:


year = data['work_year']
stats = {'sum':year.sum(), #showing  the sum of column work_year
         'mean':year.mean(), #showing  the mean of column work_year
         'standard deviation':year.std(), #showing  the standard deviation of column work_year
         'skewness':year.skew(), #skewness of column work_year
         'kurtosis':year.kurtosis() #kurtosis of column work_year
        }
         
stats #printing the variable


# ## Question 2

# ### Write a Python program to calculate and show correlation of all variables.

# In[26]:


data.corr(numeric_only=True) # Displaying correlation of numeric value only because correlation cannot be shown for String value


# # Data Exploration

# ## Question 1

# ### Write a python program to find out top 15 jobs. Make a bar graph as well.

# In[27]:


top_15_job = data['job_title'].value_counts().head(15) #Counting the occurence of unique job title in the column and showing top 15 
top_15_job # printing the output


# In[47]:


top_15_job.plot(kind='bar', title= 'Top 15 Jobs') # Plotting Bar Graph for top 15 jobs
plt.xlabel('Jobs Title') # Giving the X-axis name Job title
plt.ylabel('Value Counts') # Giving the Y-axis name Value Counts
plt.legend() # Display legend 


# ## Question 2

# ### Which job has the highest salaries? Illustrate with bar graph.

# In[68]:


max_salary = data.loc[data.groupby('job_title')['salary_in_usd'].idxmax(), ['job_title', 'salary_in_usd']]
# Using loc to retrieve only two column data which is grouped by job_title column
# And displaying on max salary from the unique job_tile with the help of index
                                                                    
max_salary = max_salary.sort_values(by='salary_in_usd', ascending=False)# sorting the values by salary_in_usd column, 
                                                        #ascending = false which will display the highest to lowest
highest_salary = max_salary.head(15) # Only Displaying top 15
highest_salary #printing the value


# In[70]:


highest_salary.plot(kind='bar',x='job_title', title= 'Job Having Highest Salary', color='red')
# Displaying Bar Graph with giving the x value because it will display index in x axis along with title and different color
plt.xlabel('Jobs') # Giving the X-axis name Jobs
plt.ylabel('Salaries') # Giving the Y-axis name Salary
plt.legend() # Display legend 


# ## Question 3

# ### Write a python program to find out salaries based on experience level. Illustrate it through bar graph.

# In[60]:


salary_experience = data.loc[data.groupby('experience_level')['salary_in_usd'].idxmax(),['experience_level','salary_in_usd']]
# Retrieving only experience_level and salary_in_usd column value which is group and experience level and 
# highest salary of that experiencelevel with the help of index

salary_experience # printing the output


# In[71]:


salary_experience.plot(kind='bar', x = 'experience_level', title = "Salary Based on experience level", color="green") 
# Displaying Bar Graph with giving the x value because it will display index in x axis along with title and different color
plt.xlabel('Experience_Level') # Giving the X-axis name Experience Level
plt.ylabel('Salary') # Giving the Y-axis name Salary
plt.legend()


# ## Question 4

# ### Write a Python program to show histogram and box plot of any chosen different variables. Use proper labels in the graph.

# In[64]:


fig, (figure_1, figure_2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
# Creating a figure with two subplots arranged horizontally

figure_1.hist(data['work_year'], bins=len(data['work_year'].unique()), edgecolor='black', color='red')
# Plotting a histogram of the 'work_year' column in the first subplot

figure_1.set_title('Year Histogram')
# Setting title for the first subplot

figure_1.set_xlabel('Year') # Giving the X-axis name Year
figure_1.set_ylabel('Value Counts') # Giving the Y-axis name Value Counts

figure_2.hist(data['salary_in_usd'], edgecolor='black',color='green')
# Plotting a histogram of the 'salary_in_usd' column in the second subplot

figure_2.set_title('Salary Histogram')
# Setting title for the second subplot

figure_2.set_xlabel('Salary in USD') # Giving the X-axis name Salary in Usd
figure_2.set_ylabel('Value Count') # Giving the Y-axis name Value Counts


# In[75]:


plt.boxplot(data['salary_in_usd']) # Creating box plot
plt.title('Boxplot of Salary in USD') # Giving the title name Salary in USD
plt.xlabel('Salary Distribution') # Giving the X-axis name Salary distribution
plt.ylabel('Salary (USD)') # Giving the Y-axis name Salary (USD)


# In[82]:


plt.boxplot(data['work_year']) # Creating box plot
plt.title('Boxplot of work year') # Giving the title name Salary in USD
plt.xlabel('year') # Giving the X-axis name Salary distribution
plt.ylabel('work year') # Giving the Y-axis name Salary (USD)


# In[ ]:




