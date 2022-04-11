from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(User):
    # username
    # password
    # email
    # first_name
    # last_name
    
    def __str__(self):
        return self.username