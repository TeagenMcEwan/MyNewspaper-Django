from django.db import models
from django.contrib.auth.models import AbstractUser


# Use this section to add a profile pic or bio. 

class CustomUser (AbstractUser):
    pass #this is where I would put my own files

    def __str__(self):
        return self.username




