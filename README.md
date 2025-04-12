# Task management app Step-by-step

This repository contains a Task Management Application created as a learning project to gain hands-on experience with Python (Django), RESTful API development, AWS cloud services, and containerization with Docker. The goal is to build a functional application while documenting the process and demonstrating understanding of these technologies.

## Tool used for this project

* Python
* Pip
* Virtualenv
* Django

## Step 1 - Set Up the Local Development Environment

### Task 1: Installation and set up

1. Clone the repository into the local environment

    ```bash
    git clone https://github.com/Estebra/task-management-app.git
    ```

2. Create the the virtual environment insided the repostory

    ```bash
    virtualenv venv
    ```

3. Activate the virtual environment

    ```bash
    source venv/bin/activate
    echo $VIRTUAL_ENV
    ```

4. Install Django into the virtual environment

    ```bash
    pip3 install Django
    ```

### Task 2: Project structure

1. Run the Django command to create the new project

    ```bash
    django-admin startproject task_management_project .
    ```

2. Build the first app in Django

    * Run the Django command to create a new app name "tasks"

        ```bash
        python manage.py startapp tasks
        ```

## Step 2 - Database Design and Setup

### Task 1: Design the Task model

Defining the fields the Task object will have.

1. Open the tasks/model.py in a code editor
    This is where the structure of the "Task" data is define.

2. Make sure you import the base classes and tools:

    ```python
    from django.db import models
    ```

3. Define the Task model:

    By inheriting from models.Model, tells Django that this represents a database table

    ```python
    class Task(models.Model):
    ```

4. Set the attributes that will define the task model: The structure of this attributs is `atributeName = importedMudule.FieldType(parameters)`

    ```python
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, mull=True)
    ```

5. The attribute "status" will have a list of coubles, for which we set 3 options to choose from and a default option:

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

6. For the dates we make sure they are set to be added and updated in the respective attributes to make sure we can track the changes in the tasks:

    ```python
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DatetimeField(auto_now=True)
    ```

7. Now we create a method that returns a string with the name of the "title attribute when the object is printed:

    ```python
    def __str__(self): 
        return self.title
    ```

    > [Complete code of the Step 2: Task 1](tasks/models.py)

8. Django needs to be told that the tasks app exists by adding it to the INSTALLED_APPS list in the projec's settings.py file.

    * Open the task_management_project/settings.py file.
    * Locate the INSTALLED_APPS list.
    * Add the name of the app, 'tasks' (as a string).
    * Save the file and try to run the command once more.

        ```python
        # Application definition

            INSTALLED_APPS = [
                'tasks',
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
            ]
        ```

### Task 2: Choosing and Configuring the Database

1. Install the PostgreSQL Adapter: Used by Django (database adapters) to connect to specific database systems. PostgreSQL needs the psycopg2 package.

   * Run the following command to install the psycog2 adapter:

        ```bash
        pip install psycopg2-binary
        ```

2. Configure Django for PostgreSQL: Django needs to be told to use PostgreSQL.
   * Modify the DATABASE settings in the project's setting.py file.
   * Open [task_management_project/settings.py](task_management_project/settings.py).
   * Locate the DATABASE dictionary, and replace the content of the DATABASE dictionary with the configuration for PostgreSQL.

        ```python
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'dbname',
                'USER': 'db_user',
                'PASSWORD': 'password',
                'HOST': 'db-AWS-RDS-Endpoint', # replace with the AWS RDS endpoint
                'PORT': '5432', # default PostgreSQL port
            }
        }
        ```

3. Create and Apply Database Migrations.

    * Migration are how Django handles changes to your models in the database schema, the Task model define in the tasks/medels.py. We need to create a migration for it and apply that migration for the tasks app.
    * Run the following command to create the migrations for the tasks app:

        ```bash
        python manage.py makemigrations tasks
        ```

        * "0001_initial.py" output tell that Django has detected the changes made in the Task model and has created a new migration file in the tasks/migrations directory.

        _After last step we should have run `python manage.py migrate` but but if we do not have PostgreSQL installed the migrate command will fall with a OperationError when trying to connect to the server. We will fix this once the AWS DB is set up ond configure the correct connection details in the settings.py file._

__EXTRA__

## Step 3 - Setting up PostgreSQL on AWS

1. Log into the AWS Management Console
2. Navigate to the RDS service
3. Choose   `Create database`
4. Select the `PostgreSQL` engine type
5. Choose a use case (Dev in this case)
6. Specify database details:

    * Selecting the free tier and the db.t4g.micro that has a cost-effective and the efficiency of Graviton2.
    * Storage General Purpose SSD with 20Gib

7. Configure the network and Security:

     * Publicly accessible: For simplicity in this learning phase, we are choosing "Yes". However, for production environments, it's generally recommended to keep databases private and access them through other AWS services.

Take note of the Enpoint, this is the hostname we will use to connect to the database.

## Step 4 - Connecting Django to the AWS PostgreSQL DB

We will update the Django project's settings to connect to the newly created PostgreSQL database on AWS.

1. Open your tastk_management_project/setting.py file.
2. Modify the DATABASE setting to reflect your AWS PostgreSQL instance details.

This will tell Django to communicate with the PostgreSQL database on AWS.

## Step 5 - Running Migration on the AWS DB

Now we can run the Django migrations to crate the necessary tables in our AWS PostgreSQL database based on the tasks/medels.py file.

1. Run the migration command:

    ```bash
    python manage.py migrate
    ```

__EXTRA__

## Step 6 - Implementing RESTful API Endpoints with Django REST Framework

Now we define the API Endpoint to perform CRUD operations on our tasks. We will use Django REST Framework.

1. Install Django REST Framework:

    ```bash
    pip install djangorestframework
    ```

2. Add the ‘rest_framework’ to the INSTALLED_APPS in task_managment_project/settings.py:

    ```python
    # Application definition

        INSTALLED_APPS = [
            'rest_framework',
            'tasks',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
    ```

3. Create a serialiver.py file within your tasks app directory. This will define how the Task model instances should be converted to JSON (and vice versa). Add the following code:

    ```bash
    touch tasks/serializers.py
    ```

    ```python
    # tasks/serializers.py
    from rest_framework import serializers
    from .models import Task

    class TaskSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = '__all__' # include all fields from the Task model
    ```

4. The tasks/views.py will contain the logic for the API endpoint. We are using the Django Framework’s ModelViewSet for easy CRUD operations:

    ```python
    from django.shortcuts import render

    # Create your views here.

    from rest_framework import viewsets
    from .models import Task
    from .serializers import TaskSerializer

    class TaskViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows tasks to be viewed or edited.
        """
        queryset = Task.objects.all()
        serializer_class = TaskSerializer
    ```

## Step 7 - Testing the API Endpoints

We will now test our newly created API endpoints to ensure they are working correctly.

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Using curl in the terminal to send a HTTP request to the following endpoints:

    * GET <http://127.0.0.1:8000/api/tasks/> : To retrieve a list of all tasks (should be empty initially):

    ```bash
    curl
    ```

    * POST <http://127.0.0.1:8000/api/tasks/> : To create a new task. Send a JSON payload in the request body like:

    ```bash
    curl
    ```

    * GET <http://127.0.0.1:8000/api/tasks/{id}/> : Replace {id} with the ID of the task you just created to retrieve that specific task:

    ```bash
    curl
    ```

    * PUT <http://127.0.0.1:8000/api/tasks/{id}/> : Replace {id} with the task ID to update the task. Send a JSON payload with the updated information.

    ```bash
    curl
    ```

    * DELETE <http://127.0.0.1:8000/api/tasks/{id}/> : Replace {id} with the task ID to delete the task.

Now we are able to create, read, update, and delete tasks through your RESTful API.
