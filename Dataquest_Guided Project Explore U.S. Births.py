
# coding: utf-8

# In[1]:

births_string = open("US_births_1994-2003_CDC_NCHS.csv", 'r').read()
births_list = []
births_list = births_string.split("\n")

    


# In[3]:

def read_csv(filename):
    string_data = open(filename).read()
    string_list = string_data.split("\n")[1:]
    final_list = []
    
    for row in string_list:
        string_fields = row.split(",")
        int_fields = []
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list
        
cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


# In[4]:

cdc_list[0:10]


# In[5]:

def month_births(data):
    births_per_month = {}
    
    for row in data:
        month = row[1]
        births = row[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    return births_per_month

cdc_months_births = month_births(cdc_list)


# In[6]:

cdc_months_births


# In[7]:

def dow_births(data):
    births_per_dow = {}
    
    for row in data:
        dow = row[3]
        births = row[4]
        if dow in births_per_dow:
            births_per_dow[dow] = births_per_dow[dow] + births
        else:
            births_per_dow[dow] = births
    return births_per_dow
    
cdc_dow_births = dow_births(cdc_list)


# In[8]:

cdc_dow_births


# In[11]:

def calc_counts(data, column):
    number_of_births = {}
    
    for row in data:
        column_value = row[column]
        births = row[4]
        if column_value in number_of_births:
            number_of_births[column_value] += births
        else:
            number_of_births[column_value] = births
    return number_of_births

cdc_year_births = calc_counts(cdc_list, 0)
cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)
    


# In[12]:

cdc_year_births


# In[ ]:



