#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[1]:


from faker import Faker
import random
from random import randint
import csv


# # Data Generator Function

# In[2]:


def datagen(np, parameters):
    fake = Faker()
    with open("Data_generator.csv", 'wt', newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=parameters)
        writer.writeheader() 
        for i in range(np):
            ph1=str(random.randint(0,999))
            ph2=str(random.randint(0,999)).zfill(3)
            ph3=str(random.randint(0,9999)).zfill(4)
            phone_number="{}-{}-{}".format(ph1,ph2,ph3)
            
            writer.writerow({
                "Student Name": fake.name(),
                "Country": fake.country(),
                "Course Comments": fake.text(),
                "Student ID": randint(1, 99999),
                "Email Id": fake.email(),
                "Phone Number": phone_number,
                "Date of Birth": random.randint(1950,2010),
                "House Address": fake.address(),
                "Latitude": fake.latitude(),
                "Longitude": fake.longitude()
            })          


# # Function Call

# In[3]:


if __name__ == '__main__':
    np = int(input(" Enter Number of Student Data:"))
    parameters = ["Student ID", "Student Name", "Email Id", "Phone Number", "Date of Birth", "House Address",
               "Latitude", "Longitude", "Country", "Course Comments"]
    datagen(np, parameters)
    print("File saved.")


# In[ ]:




