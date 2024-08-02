from django.db import models
from .conversations import Conversations

class Files(models.Model):
    file_id = models.UUIDField(null=False, unique=True)
    conversation = models.ForeignKey(Conversations, null=True, on_delete=models.CASCADE)    
    name = models.CharField(max_length=20, null=False)
    summary = models.CharField(max_length=4000, null=False) 
    
    class Meta:
        db_table = "files"
        verbose_name = "files"
