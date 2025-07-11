# -*- coding: utf-8 -*-
"""CustomerConversion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OanvHbOVDo2U8U9FMOddheH9jDLYtjOz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

"""# Processing and going through the database"""

df=pd.read_csv("train.csv")

print("Data set size : ", df.shape)

df.head()

df.tail()

df.columns

df.describe()

"""Checking whether the database is balanced"""

df['y'].value_counts()

print('Percentage for "no": ',((39916) / (39916+5289)) * 100 )
print('Percentage for "yes": ',((5289) / (39916+5289)) * 100 )

"""Identifying and Eliminating the NULL values"""

df.isnull().sum()

df.duplicated().sum()

df = df.drop_duplicates()

df.dtypes

"""Identifying unique values in each attribute"""

print("Unique values of Job \n")
print(df['job'].unique())
print("\n")

print("Unique values of Marital Status \n")
print(df['marital'].unique())
print("\n")

print("Unique values of Educationsl Qualification \n")
print(df['education_qual'].unique())
print("\n")

print("Unique values of Call Type \n")
print(df['call_type'].unique())
print("\n")

print("Unique values of Month \n")
print(df['mon'].unique())
print("\n")

print("Unique values of Previous Outcome \n")
print(df['prev_outcome'].unique())
print("\n")

print("Unique values of Target Variable 'y' \n")
print(df['y'].unique())

"""Replacing categorical target data into numeric values"""

df['target'] = df["y"].map({"yes":1 , "no": 0})
df.head()

"""# Calculating count for each attribute and comparing its percentage with the target, Changing unknown attribute to NULL and then dropping all the NULL values

### for age:
"""

df.age.value_counts()

df.groupby('age')['target'].mean()

"""### for job:"""

df.job.value_counts()

df.groupby('job')['target'].mean()

df['job'] =df['job'].replace('unknown',np.nan)

df.job.isnull().sum()

df=df.dropna(subset=['job'])

df.job.isnull().sum()

"""### for marital status:"""

df.marital.value_counts()

df.groupby('marital')['target'].mean()

"""### for educational qualification:"""

df.education_qual.value_counts()

df.groupby('education_qual')['target'].mean()

print('Percentage for "Unknown": ',((1730) / (23202+13301+6851+1730)) * 100 )

df['education_qual'] =df['education_qual'].replace('unknown',np.nan)
df.education_qual.isnull().sum()

df = df. dropna(subset=['education_qual'])
df.education_qual.isnull().sum()

"""### for call type:"""

df.call_type.value_counts()

df.groupby('call_type')['target'].mean()

print('Percentage for "Unknown": ',((12283) / (29285+13020+12283)) * 100 )

"""### for day of the month:"""

df.day.value_counts()

df.groupby('day')['target'].mean()

"""### for month:"""

df.mon.value_counts()

df.groupby('mon')['target'].mean()

"""### for duration of the call:"""

df.dur.value_counts()

df.groupby('dur')['target'].mean()

"""### for number of calls:"""

df.num_calls.value_counts()

df.groupby('num_calls')['target'].mean()

"""### for previous outcome of success:"""

df.prev_outcome.value_counts()

df.groupby('prev_outcome')['target'].mean()

print('Percentage for "Unknown": ',((35280) / (35280+4709+1774+1424)) * 100 )

"""### for attribute column Y:"""

df.y.value_counts()

#Checking Final dataframe, with no null values
df.info()

"""# Outlier detection and correction by either stirp(clip function) or complete deletion"""

df.info()

"""### for age:"""

#plotting boxplot to visualize presence of outliers
sns.set(style="whitegrid")
sns.boxplot(x=df['age'], color='Chartreuse')

q1,q3=np.percentile(df["age"],[25,75])
IQR=q3-q1
upper=q3+1.5*IQR
lower=q1-1.5*IQR
print("Upper age bound:",upper,"Lower age bound :", lower)

df.age = df.age.clip(10.5,70.5)

df.age.describe()

#boxplot after outlier correction
sns.set(style="whitegrid")
sns.boxplot(x=df['age'], color='Chartreuse')

"""### for day:"""

sns.set(style="whitegrid")
sns.boxplot(x=df['day'], color='Chartreuse')

q1,q3=np.percentile(df["day"],[25,75])
IQR=q3-q1
upper=q3+1.5*IQR
lower=q1-1.5*IQR
print("Upper bound:",upper,"Lower bound :", lower)

df.day.describe()

"""### for duration of call:"""

sns.set(style="whitegrid")
sns.boxplot(df['dur'], color='Chartreuse')

q1,q3=np.percentile(df["dur"],[25,75])
IQR=q3-q1
upper=q3+1.5*IQR
lower=q1-1.5*IQR
print("Upper bound:",upper,"Lower bound :", lower)

df.dur = df.dur.clip(-219.5,640.5)

df.dur.describe()

sns.set(style="whitegrid")
sns.boxplot(df['dur'], color='Chartreuse')

"""### for number of calls:"""

sns.set(style="whitegrid")
sns.boxplot(df['num_calls'], color='Chartreuse')

q1,q3=np.percentile(df["num_calls"],[25,75])
IQR=q3-q1
upper=q3+1.5*IQR
lower=q1-1.5*IQR
print("Upper bound:",upper,"Lower bound :", lower)

df.num_calls = df.num_calls.clip(-2,6.0)

df.num_calls.describe()

sns.set(style="whitegrid")
sns.boxplot(df['num_calls'], color='Chartreuse')

"""# EDA (exploratory Data Analysis) to identify issues and develop deeper understanding of relationship within variables

### Distribution graph of all numerical varibales with the count value
"""

# Age distribution
plt.figure(figsize = (40,30),dpi=200)
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, wspace=0.5, hspace=0.3)
plt.subplot(3,4,1)
sns.histplot((df.age),color='BlueViolet')

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['age']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Age Distribution', fontsize = 12, color='maroon', fontweight='bold')
plt.xlabel('Age',fontsize = 12, color='green')
plt.ylabel('Count',fontsize = 12, color='green')




#Job distribution
plt.subplot(3,4,2)
sns.countplot(df['job'],order=df.job.value_counts().index)

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['job']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, ha='center', va='bottom', color='Purple')

plt.title('Job Distribution', fontsize = 14, color="maroon", fontweight='bold')
plt.xlabel('Type Of Job',fontsize = 12, color='green')
# plt.xticks(rotation = 90)
plt.ylabel('Count',fontsize = 12, color='green')



# Marital distribution
plt.subplot(3,4,3)
custom_colors = {'married': 'Magenta', 'divorced': 'BlueViolet', 'single': 'Lime'}
sns.countplot(df['marital'],order=df.marital.value_counts().index, palette=custom_colors)

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['marital']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Marital Status Distribution', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Marital',fontsize = 12, color='green')
plt.xticks(rotation = 90)
plt.ylabel('Count',fontsize = 12, color='green')



# Education qualification distribution
plt.subplot(3,4,4)
custom_colors = {'secondary': 'DarkGreen', 'tertiary': 'LightSeaGreen', 'primary': 'Aquamarine'}
sns.countplot(df['education_qual'],order=df.education_qual.value_counts().index, palette=custom_colors)

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['education_qual']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Education Qualification', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Education',fontsize = 12, color='green')
plt.xticks(rotation = 90)
plt.ylabel('Count',fontsize = 12, color='green')




# Call type distribution
plt.subplot(3,4,5)
custom_colors = {'cellular': 'MediumVioletRed', 'telephone': 'purple', 'unknown' :'MediumSpringGreen'}
sns.countplot(df['call_type'],order=df.call_type.value_counts().index, palette=custom_colors)

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['call_type']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Call Type', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Call type',fontsize = 12, color='green')
plt.xticks(rotation = 90)
plt.ylabel('Count',fontsize = 12, color='green')




# Day distribution
plt.subplot(3,4,6)
sns.histplot(df['day'], color="Fuchsia")

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['day']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Day', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Day',fontsize = 12, color='green')
plt.xticks(rotation = 90,fontsize = 10)
plt.ylabel('Count',fontsize = 12, color='green')




 # Mon distribution
plt.subplot(3,4,7)
sns.countplot(df['mon'],order=df.mon.value_counts().index)

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['mon']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Month', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Month',fontsize = 12, color='green')
plt.xticks(rotation = 90)
plt.ylabel('Count',fontsize = 12, color='green')




# Dur distribution
plt.subplot(3,4,8)
sns.histplot((df.dur),color = 'cyan')

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['dur']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Duration', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Duration',fontsize = 12, color='green')
plt.ylabel('Count',fontsize = 12, color='green')




# Num call distribution
plt.subplot(3,4,9)
sns.histplot(df['num_calls'])

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['num_calls']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Number Of Calls', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Number Of Calls',fontsize = 12, color='green')
plt.xticks(rotation = 90)
plt.ylabel('Count',fontsize = 12, color='green')


# Previous outcome distribution
plt.subplot(3,4,10)
custom_colors = {'unknown': 'HotPink', 'failure': 'Olive', 'other': 'Purple', 'success':'Yellow'}
sns.countplot(df['prev_outcome'],order=df.prev_outcome.value_counts().index, palette=custom_colors)

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['prev_outcome']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Previous Outcome', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Previous Outcome',fontsize = 12, color='green')
plt.xticks(rotation = 90)
plt.ylabel('Count',fontsize = 12, color='green')


 # Target distribution
plt.subplot(3,4,11)
custom_colors = {'no': 'GreenYellow', 'yes': 'Teal'}
sns.countplot(df['y'], palette=custom_colors)

# Get the current Axes object
ax = plt.gca()

# Calculate and annotate the percentage of each category
total = float(len(df['y']))
for p in ax.patches:
    height = p.get_height()
    percentage = '{:.1f}%'.format(100 * height/total)
    x = p.get_x() + p.get_width() / 2 - 0.1
    y = height + 5
    ax.text(x, y, percentage, fontsize=8, rotation=90, ha='center', va='bottom', color='Purple')

plt.title('Target Distribution', fontsize = 14, color='maroon', fontweight='bold')
plt.xlabel('Target Distribution',fontsize = 12, color='green')
plt.xticks(rotation = 90)
plt.ylabel('Count',fontsize = 12, color='green')

# plt.tight_layout()


plt.show()

"""### Distribution graph of all numerical values with the target value"""

plt.figure(figsize=(20,35), dpi=180)
#plt.suptitle("Categorical Data Vs Target", fontsize=20, fontweight='bold', color='maroon')
#Jobs vs Target
plt.subplot(3,3,1)
my_colors = ['Magenta', 'cyan']
sns.countplot(x='job',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Jobs vs Target', fontweight='bold', color='maroon')
plt.xlabel('Job', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Marital Status vs Target
plt.subplot(3,3,2)
my_colors = ['Magenta', 'cyan']
sns.countplot(x='marital',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Marital Status vs Target', fontweight='bold', color='maroon')
plt.xlabel('Marital Status', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Educational Qualification vs Target
plt.subplot(3,3,3)
my_colors = ['Magenta', 'cyan']
sns.countplot(x='education_qual',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Educational Qualification vs Target', fontweight='bold', color='maroon')
plt.xlabel('Educational Qualification', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Month vs Target
plt.subplot(3,3,4)
my_colors = ['Magenta', 'cyan']
sns.countplot(x='mon',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Month vs Target', fontweight='bold', color='maroon' )
plt.xlabel('Month', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Previous Outcome vs Target
plt.subplot(3,3,5)
my_colors = ['Magenta', 'cyan']
sns.countplot(x='prev_outcome',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Previous Outcome vs Target', fontweight='bold', color='maroon' )
plt.xlabel('Previous Outcome', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Call Type vs Target
plt.subplot(3,3,6)
my_colors = ['Magenta', 'cyan']
sns.countplot(x='call_type',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Call Type vs Target', fontweight='bold', color='maroon')
plt.xlabel('Call Type', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

plt.show()

plt.figure(figsize=(20,35), dpi=180)
#plt.suptitle("Categorical Data Vs Target", fontsize=20, fontweight='bold', color='maroon')

#Jobs vs Target
plt.subplot(3,3,1)
(df.groupby('job')['target'].mean()*100).sort_values().plot(kind="bar",color='cyan')
plt.xticks(rotation=50)
plt.title('Jobs vs Target', fontweight='bold', color='maroon')
plt.xlabel('Job', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Marital Status vs Target
plt.subplot(3,3,2)
(df.groupby('marital')['target'].mean()*100).sort_values().plot(kind="bar",color='Magenta')
plt.xticks(rotation=50)
plt.title('Marital Status vs Target', fontweight='bold', color='maroon')
plt.xlabel('Marital Status', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Educational Qualification vs Target
plt.subplot(3,3,3)
(df.groupby('education_qual')['target'].mean()*100).sort_values().plot(kind="bar",color='cyan')
plt.xticks(rotation=50)
plt.title('Educational Qualification vs Target', fontweight='bold', color='maroon')
plt.xlabel('Educational Qualification', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Month vs Target
plt.subplot(3,3,4)
(df.groupby('mon')['target'].mean()*100).sort_values().plot(kind="bar",color='Magenta')
plt.xticks(rotation=50)
plt.title('Month vs Target', fontweight='bold', color='maroon' )
plt.xlabel('Month', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Call Type vs Target
plt.subplot(3,3,5)
(df.groupby('call_type')['target'].mean()*100).sort_values().plot(kind="bar",color='cyan')
plt.xticks(rotation=50)
plt.title('Call Type vs Target', fontweight='bold', color='maroon')
plt.xlabel('Call Type', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#Previous Outcome vs Target
plt.subplot(3,3,6)
(df.groupby('prev_outcome')['target'].mean()*100).sort_values().plot(kind="bar",color='Magenta')
plt.xticks(rotation=50)
plt.title('Previous Outcome vs Target', fontweight='bold', color='maroon')
plt.xlabel('Previous Outcome', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')


plt.show()

plt.figure(figsize=(20, 15), dpi=150)
#sub title to show title for overall plot
plt.suptitle("Numerical Data Vs Target", fontsize=18,  fontweight='bold', color='maroon')

#Age vs Target
plt.subplot(2,2,1)
my_colors = ['Magenta', 'DarkBlue']
sns.histplot(x='age',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Age vs Target', fontweight='bold', color='maroon' )
plt.xlabel('Age', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')
#df[['age','target']].corr()

#Day vs Target
plt.subplot(2,2,2)
my_colors = ['Magenta', 'DarkBlue']
sns.histplot(x='day',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Day vs Target', fontweight='bold', color='maroon' )
plt.xlabel('Day', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')
#df[['day','target']].corr()

#Duration vs Target
plt.subplot(2,2,3)
my_colors = ['Magenta', 'DarkBlue']
sns.histplot(x='dur',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('Duration vs Target', fontweight='bold', color='maroon' )
plt.xlabel('Duration', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

#No of Calls vs Target
plt.subplot(2,2,4)
my_colors = ['Magenta', 'DarkBlue']
sns.histplot(x='num_calls',hue='y',data=df, palette=my_colors)
plt.xticks(rotation=50)
plt.title('No of Calls vs Target', fontweight='bold', color='maroon' )
plt.xlabel('No Of Calls', color='DarkGreen')
plt.ylabel('y', color='DarkGreen')

plt.show()

"""# Encoding"""

df.columns

"""job column:"""

df['job']=df['job'].map({'blue-collar':1,'entrepreneur':2,'services':3,'housemaid':4,'technician':5,'self-employed':6,'admin.':7,'management':8, 'unemployed':9, 'retired': 10, 'student' : 11})
df.head(3)

"""Marital Status column:"""

df['marital'] =df['marital'].map({'married': 1, 'divorced': 2, 'single' : 3})
df.head(3)

"""Educational qualification column:"""

df['education_qual'] = df['education_qual'].map({'primary': 1, 'secondary': 2, 'tertiary' :3})
df.head(3)

"""Month column"""

df['mon']=df['mon'].map({'may': 1, 'jul' : 2, 'jan': 3, 'nov': 4, 'jun' : 5, 'aug' : 6, 'feb' : 7, 'apr' : 8, 'oct' : 9, 'dec' : 10 , 'sep': 11, 'mar': 12})
df.head(3)

"""Call type column:"""

df['call_type'] = df['call_type'].map({'unknown': 1, 'telephone' : 2, 'cellular' : 3})
df.head(3)

"""previous outcome column:"""

df['prev_outcome']=df['prev_outcome'].map({'unknown' : 1, 'failure' : 2, 'other' : 3, 'success': 4})
df.head(3)

"""# Splitting, Balancing and Scaling the data to be used in ML models"""

df.columns

x = df[['age', 'job', 'marital', 'education_qual', 'call_type', 'day', 'mon', 'dur', 'num_calls', 'prev_outcome']].values
y=df['target'].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state = 3 )

#Balancing the data
from imblearn.combine import SMOTEENN
smt = SMOTEENN(sampling_strategy='all')
x_train_smt, y_train_smt = smt.fit_resample(x_train, y_train)

print(len(x_train_smt))
print(len(y_train_smt))

#scaling the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train_smt)
x_test_scaled = scaler.transform(x_test)

"""# Implementation of ML models

### Logistic regression
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

lr = LogisticRegression()

lr.fit(x_train_scaled,y_train_smt)
lr.score(x_test_scaled,y_test)

y_pred=lr.predict_proba(x_test_scaled)
y_pred

log_reg_auroc = roc_auc_score(y_test,y_pred[:,1])
print("AUROC score for logistic regression  :  ",round(log_reg_auroc,2))

"""### KNN (K-Nearest Neighbours)"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
for i in [1,2,3,4,5,6,7,8,9,10,20,30,40,50]:
  knn= KNeighborsClassifier(i)
  knn.fit(x_train_scaled, y_train_smt)
  print("K value :", i, "Train Score : ", knn.score(x_train_scaled,y_train_smt), "Cross Value Accuracy :" , np.mean(cross_val_score(knn, x_test_scaled, y_test, cv=10)))

knn= KNeighborsClassifier(i)
knn.fit(x_train_scaled, y_train_smt)
print("KNN Score: ",knn.score(x_test_scaled,y_test))
print( "AUROC on the sampled dataset : ",roc_auc_score( y_test, knn.predict_proba(x_test)[:, 1]))

"""### Decision Tree"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
dt = DecisionTreeClassifier()
dt.fit(x_train_smt,y_train_smt)
print("Decision Tree Score : ", dt.score(x_train_smt,y_train_smt))
print( "AUROC on the sampled dataset : ",roc_auc_score( y_test, dt.predict_proba(x_test)[:, 1]))

from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import cross_val_score
import numpy as np

for depth in [1,2,3,4,5,6,7,8,9,10,20]:
  dt = DecisionTreeClassifier(max_depth=depth)
  # Fiting dt to the training set
  dt.fit(x_train_smt, y_train_smt)
  trainAccuracy = accuracy_score(y_train_smt, dt.predict(x_train_smt)) # this isn't reliable information - i am printing the training accuracy check the difference between this and crossval
  dt = DecisionTreeClassifier(max_depth=depth) # a fresh model which is not trained yet (for cross validation)
  valAccuracy = cross_val_score(dt, x_test_scaled, y_test, cv=10)
  print("Depth  : ", depth, " Training Accuracy : ", trainAccuracy, " Cross val score : " ,np.mean(valAccuracy))

dt = DecisionTreeClassifier(max_depth=5)
dt.fit(x_train_smt,y_train_smt)
print("Decision Tree Score : ", dt.score(x_train_smt,y_train_smt))
print( "AUROC on the sampled dataset : ",roc_auc_score( y_test, dt.predict_proba(x_test)[:, 1]))

"""### XGBoost"""

import xgboost as xgb
from sklearn.model_selection import cross_val_score
import numpy as np
for lr in [0.01,0.02,0.03,0.04,0.05,0.1,0.11,0.12,0.13,0.14,0.15,0.2,0.5,0.7,1]:
  model = xgb.XGBClassifier(learning_rate = lr, n_estimators=100, verbosity = 0)
  model.fit(x_train_smt,y_train_smt)
  print("Learning rate : ", lr," Train score : ", model.score(x_train_smt,y_train_smt)," Cross-Val score : ", np.mean(cross_val_score(model, x_test, y_test, cv=10)))

"""### Random forest"""

from sklearn.ensemble import RandomForestClassifier
rf= RandomForestClassifier(max_depth=2,n_estimators=100,max_features="sqrt")
rf.fit(x_train, y_train)
y_pred= rf.predict(x_test)

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
for depth in [1,2,3,4,5,6,7,8,9,10]:
  rf= RandomForestClassifier(max_depth=depth,n_estimators=100,max_features="sqrt")
  rf.fit(x_train, y_train)
  rf= RandomForestClassifier(max_depth=depth,n_estimators=100,max_features="sqrt")
  valAccuracy = cross_val_score(rf, x_train, y_train, cv=10)
  print("Depth  : ", depth, " Training Accuracy : ", trainAccuracy, " Cross val score : " ,np.mean(valAccuracy))

"""**Therefore, The highest accuracy was achieved via random forest. with the final cross validation score of 0.90 accuracy**

# Feature importance
"""

from xgboost import plot_importance

plot_importance(model)
plt.show()
df.columns

"""*where, features are indexed as f0=age, f1=job, f2= marital, etc.
Therefore, according to the feature importance plot, f7 is most effective i.e duration of the call.*

---
"""