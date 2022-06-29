from django.db import models
from accounts.models import CustomUser
class Chat(models.Model):

    class Meta:

        db_table = 'chat'
    
    from_message = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    message = models.CharField(max_length=1000)
    to_message = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')