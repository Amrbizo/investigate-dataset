#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset - [No-show appointments]
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# > 
# I am working on [No-show appointments] to have an insight about why the people did not show what are the common illlness, if the scholarship playing a role, if this initive has made an impact, discovering if notifying way used was effiecent enough to reach out for the patients.
# The dataset has AppointmentID,Gender,ScheduledDay,AppointmentDay,Age,Neighbourhood,Scholarship,Hipertension,Diabetes,Alcoholism,Handcap,SMS_recived,No-show coulmns 
# the appointment id , scheduledDay, Appointment day are adminstrative info the other coulmns will be very benefical in our analysis
# 
# 
# ### Question(s) for Analysis
# >
# one of the questions which provoked me to do the analysis on this dataset, if te patients recived sms with the appointment info, and if yes how could we optimize this process.
# Also the relationship between the scholarship holders and the the attendees, if no i want to encourage more of this initiave in the future specailly in the poorest neigbourhood in Brazil.
# IS there any relationship between the above mentioned illness and the gender of the attendees .
# 
# 

# In[141]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > 
# the data were clean with no NaN values i did not fill any not number values, i only removed the unnecessary coulmns .
# 
# 

# In[281]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df = pd.read_csv('noshowappointments-kagglev2-may-2016.csv')
df.info()
df.head()


# 
# ### Data Cleaning
# > **Tip**: Make sure that you keep your reader informed on the steps that you are taking in your investigation. Follow every code cell, or every set of related code cells, with a markdown cell to describe to the reader what was found in the preceding cell(s). Try to make it so that the reader can then understand what they will be seeing in the following cell(s).
#  

# In[282]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.

df.drop(['PatientId','AppointmentID','ScheduledDay','AppointmentDay'],axis=1,inplace=True)
df.head()


# In[283]:


df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)
df.head()


# In[284]:


df = df.rename(columns={"no-show":"no_show"})
df.head()


# In[285]:


#changeing the data type of no_show to boolean 
change_dict = {"No":False,"Yes":True}


# In[286]:


df['no_show_edited'] = df['no_show'].map(change_dict)
df.info()


# In[287]:


df.describe()


# In[288]:


#creating masks to facilitate the filterung process
showed = df.no_show_edited == False
no_show = df.no_show_edited == True


# ## number of showed patients 

# In[289]:


df.no_show_edited[showed].value_counts()


# ## the number of the 10 most frequent neighbourhood

# In[323]:


df['neighbourhood'].value_counts().head(10)


# ## the number of 10 neigbourhood of most common attendees 

# In[291]:


df.neighbourhood[showed].value_counts().head(10)


# ## number of no show patients 

# In[292]:


df.no_show_edited[no_show].value_counts()


# ## the number of males and females who showed 

# In[293]:


df.groupby('gender').no_show_edited.value_counts()


# ## calcuating the number of scholarhip holder who either showed up or no show 

# In[300]:


#showed up patients with scholarships
df.scholarship[showed].sum()


# In[301]:


#no show up patients  with scholarships
df.scholarship[no_show].sum()


# ## number of sms recived patients 

# In[302]:


#number of showed up patients after reciving a notifying sms
df.sms_received[showed].sum()


# In[303]:


#number of no show patients after reciving a notifying sms 
df.sms_received[no_show].sum()


# In[306]:


#number of showed up patients 
df.no_show_edited[showed].value_counts()


# ## creating function to avoid any redundancy

# In[333]:


#creating function to evade any repititive code 
def creat_hist_info(title,xlabel,ylabel):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. **Compute statistics** and **create visualizations** with the goal of addressing the research questions that you posed in the Introduction section. You should compute the relevant statistics throughout the analysis when an inference is made about the data. Note that at least two or more kinds of plots should be created as part of the exploration, and you must  compare and show trends in the varied visualizations. 
# 
# 
# 
# > **Tip**: - Investigate the stated question(s) from multiple angles. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables. You should explore at least three variables in relation to the primary question. This can be an exploratory relationship between three variables of interest, or looking at how two independent variables relate to a single dependent variable of interest. Lastly, you  should perform both single-variable (1d) and multiple-variable (2d) explorations.
# 
# 
# ### the age distribution for the users 

# In[307]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
df.hist(figsize=(10,8));


# ## visual investiagtion of the gender number of the showed  and no showed patients 

# In[334]:


df.groupby('gender').no_show_edited.value_counts().plot(kind= 'bar');
creat_hist_info('relationship between gender and show up number','patients gender','number of patients')


# In[335]:


df['neighbourhood'].value_counts().head(10).plot(kind= 'bar');
creat_hist_info('the 10 most profitired neigbourhood','neigbourhood','number of patients')


# > it appears here clearly what the 10 most frequent neigbourhood 

# In[336]:


df.neighbourhood[showed].value_counts().head(10).plot(kind= 'bar');
creat_hist_info('the attendees from 10 most profitired neigbourhood','neigbourhood','number of patients')


# > the number of patients who alraedy showed up from the 10 most commont frequent neigbourhood

# ## female showed up more than males 

# ## number of patients received sms 

# In[337]:


df.groupby('sms_received').no_show_edited.value_counts().plot(kind= 'bar');
creat_hist_info('patients who attanded thier appointments after receiving a notifying sms','comparison between the attendees and sms reciveing','number of patients')

    


# > "its appeared here clearly that we could have  increased the amount of attendees if sms messages were recived "

# ## visualisation of the scholarship holder 

# In[338]:


df.groupby('scholarship').no_show_edited.value_counts().plot(kind= 'bar');
creat_hist_info('relationship if the attendees are scholarship holders','scholarship holders','number of patients')


# > "its appeared here that majority of the attendees are not scholarship holders, this initiation should be done more offtenly "

# ## visualisation about the gender of the scholarship holder

# In[339]:


df.groupby('scholarship').gender.value_counts().plot(kind= 'bar');
creat_hist_info('investigation about the gender of the scholarship holder','gender','number of patients')


# > "females are the most profiter of the scholarships"

# ## age distribution of the patients 

# In[340]:


df.age[showed].hist(alpha=0.5, bins=20, label='showed')
df.age[no_show].hist(alpha=0.5, bins=20, label='no_show')
plt.legend();
creat_hist_info('the age distribution of the population ','age','number of patients')


# > the age distribution of the attendees and no shows

# ## number of the showed patients for each disease

# In[341]:


#hipertension patients
df.groupby('hipertension').no_show_edited.value_counts().plot(kind= 'bar');
creat_hist_info('visual for hipertension patients','hipertension patients','number of patients')


# ## number hipertension patients who showed up and no show

# In[342]:


#diabetes patients
df.groupby('diabetes').no_show_edited.value_counts().plot(kind= 'bar');
creat_hist_info('visual for diabetes patients','diabetic patients','number of patients')


# ## number of diabetic patients who showed up and no show

# In[343]:


#number of alcohlism pateients
df.groupby('alcoholism').no_show_edited.value_counts().plot(kind= 'bar');
creat_hist_info('visual for alcohlism patients','alcoholic patients','number of patients')


# ## number of alcoholic patients 

# In[344]:


#number of handicap patients 
df.groupby('handcap').no_show_edited.value_counts().plot(kind= 'bar');
creat_hist_info('visual for handicap patients','handicaped patients','number of patients')


# > number of handicaped patients

# ## investigation for the relationship between the gender and each disease 

# In[345]:


df.groupby('diabetes').gender.value_counts().plot(kind= 'bar');
creat_hist_info('relationship between gender and diabetes','patients gender','number of patients')


# > diabetes is more common between the female attendees

# In[346]:


df.groupby('alcoholism').gender.value_counts().plot(kind= 'bar');
creat_hist_info('relationship between gender and alcoholism','patients gender','number of patients')


# > males are suffering more from alcoholism

# In[347]:


df.groupby('no_show_edited').gender.value_counts().plot(kind= 'bar');
creat_hist_info('relationship between gender and show up number','patients gender','number of patients')


# > females mostly suffering from hipertension

# <a id='conclusions'></a>
# ## Conclusions
# > I made a relationship between the scholarship holders to investigate if the scholarship was factor, i found out that most of the attendees were not scholarship holders this proves that this type of intitive is very benefical for the poor.
#  There is also an important fidnings the amount of the attendees could have been increased if the notifying sms been sent, sms and other ways of notification is very important, this should be put in mind .
# I made a relationship between the gender of the attendees.
# as limitation the analysis could have optimized more if we know the city name,it would be more insightful to know the demographic distribution of the profiters in Brazil.
# 
# ## Data cleaning 
# > The data were pretty much cleaned i just removed away the unnecessary coulmns have more insightful investigation.
# 

# In[348]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




