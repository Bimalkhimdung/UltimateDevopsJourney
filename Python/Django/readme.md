## Django 
Works as **MVT** 
- Model
- View
- Template

### Model 
- It provides data from database 
- In Django data is delivered as **ORM** ( Object Relational Mapping) 
- The models are usually located in a file called **models.py**
- Each Row in table of data is called as Objects in django

### View
- It takes http requests as arguments and look for the what data to send to template.
- The views are usually located in a file **views.py**.
### Template
- It's file where you describe how the result should be represented. Usually it contains frontend files.
- These are often ***.html*** file 
- The templates of application is located in folder name **templates**

### URLs
- In Django **URLs** is the way to navigate in different pages in websites.
- When user sends requests, Django will decide which view it will send it to.
- Files is located at *urls.py*

### Overall workflow 
when you first request the url, This basically happens:
1. Django receives the URL, checks for *urls.py* file and calls the *view* that matches the URL
2. The view, located in *view.py*, checks for relevant models.
3. The models are imported from the *model.py* file.
4. The view then sends the data to a specified template in the *template* folder.
5. The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.

### Serialization
- It's the process of converting complex data type into json data type 

### Model instance
- It's object created for model class 
for example 
```
from django.db import models

class Core(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

user_instance = Core(firstname="Bimal", lastname="Rai", email="bimal@example.com")

#Here user_instance is a model instance for class Core

#Saving into database
user_instance.save()
```
### Query set
- It represent the collection of dataset from the database.
- Here Dataset means ROWs in Database.