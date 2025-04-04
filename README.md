# Task management app Step-by-step

This repository contains a Task Management Application created as a learning project to gain hands-on experience with Python (Django), RESTful API development, AWS cloud services, and containerization with Docker. The goal is to build a functional application while documenting the process and demonstrating understanding of these technologies.

## Tool used for this project

* Python
* Pip
* Virtualenv
* Django

## Step 1 - Set Up the Local Development Environment:

### Task 1: Installation and set up
    
* Clone the repository into the local environment

```bash
git clone https://github.com/Estebra/task-management-app.git
```

* Create the the virtual environment insided the repostory 

```bash
virtualenv venv
```

* Activate the virtual environment

```bash
source venv/bin/activate
echo $VIRTUAL_ENV
```

* Install Django into the virtual environment

```bash
pip3 install Django
```

### Task 2: Project structure 

* Run the Django command to create the new project

```bash
django-admin startproject task_management_project .
```

#### Build the first app in Django

* Run the Django command to create a new app name "tasks"

```bash
python manage.py startapp tasks
```

## Step 2 - Database Design and Setup:

### Task 1: Design the Task model

Defining the fields the Task object will have.

* Open the tasks/model.py in a code editor 
    This is where the structure of the "Task" data is define.

* Make sure you import the base classes and tools:

```python
from django.db import models
```

* Define the Task model:

By inheriting from models.Model, tells Django that this represents a database table

```python
class Task(models.Model):
```

* Set the attributes that will define the task model:
    The structure of this attributs is:
    atributeName = importedMudule.FieldType(parameters)

```python
title = models.CharField(max_length=200)
description = models.TextField(blank=True, mull=True)
```

* The attribute "status" will have a list of coubles, for which we set 3 options to choose from and a default option:

```python
status = models.CharField(
    max_length=20,
    choices=[ 
        ('to_do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    default='to_do'
)
```

* For the dates we make sure they are set to be added and updated in the respective attributes to make sure we can track the changes in the tasks:

```python
due_date = models.DateTimeField(blank=True, null=True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DatetimeField(auto_now=True)

```

* Lastly we create a method that returns a string with the name of the "title attribute when the object is printed:

```python
def __str__(self): 
    return self.title
```

* [Complete code of the Step 2: Task 1](tasks/models.py)
