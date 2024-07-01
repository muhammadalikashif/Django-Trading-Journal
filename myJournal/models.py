from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from accounts.models import CustomUser

def get_default_user():
    # Replace 'your_username_here' with the actual username of the default user
    return get_user_model().objects.get(username='admin')
# Create your models here.

class Trade(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    symbol = models.CharField(max_length=100)
    entry_price = models.FloatField()
    exit_price = models.FloatField()
    result = models.CharField(max_length=10)
    observations = models.TextField((""))
    setup_image = models.ImageField(upload_to='media')
    reasons_for_entry=models.TextField((""))
    POSITION_CHOICES = [
        ('Long', 'Long'),
        ('Short', 'Short'),
    ]
    
    position = models.CharField(max_length=10, choices=POSITION_CHOICES, blank=False, default=POSITION_CHOICES[0])
    profit_loss = models.FloatField(default=0, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    def __str__(self):
        return f"{self.symbol} - {self.entry_price} - {self.setup_image}"

