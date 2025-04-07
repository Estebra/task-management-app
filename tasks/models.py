# This code defines a Django model for a task management application.
from django.db import models # Imports the base classes and tools to define the data models

# Define a Task model
class Task(models.Model): # by inheriting from models.Model, tells Django that this represents a database table

    # Structure of the atributes of the Task model
    # attributeName = importedMudule.FieldType(parameters)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        # choices takes a list of tuples
        choices=[
            ('to_do', 'To Do'), # first element is value to be stored in the database,second is human-readable name
            ('in_progress', 'In Progress'),
            ('done', 'Done')
        ],
        default='to_do'
    )
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True sets the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True) # auto_now=True updates the field to now every time the object is saved

    # python method to return a string representation of the object
    def __str__(self): 
        return self.title # it will return the title of the task when the object is printed
