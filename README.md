# task-management-app

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

### Task 1