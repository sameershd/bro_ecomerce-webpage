from django.db import models
from django.contrib.auth.models import User

#  Model for customers .


class Customer (models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICE=((LIVE,'Live'),(DELETE,'Delete'))
    name=models.CharField(max_length=200)
    adddress=models.TextField()
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name='customer_profile')
    phone=models.CharField(max_length=10)
    delete_status=models.IntegerField(choices=DELETE_CHOICE,default=LIVE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self) -> str:
        return self.name