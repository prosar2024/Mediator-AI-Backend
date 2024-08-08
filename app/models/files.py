from django.db import models
from .conversations import Conversations

class Files(models.Model):
    file_id = models.UUIDField(null=False, unique=True)
    conversation = models.ForeignKey(Conversations, null=True, on_delete=models.CASCADE)    
    unique_file_name = models.CharField(max_length=200, null=True)
    actual_file_name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=4000, null=True) 

    class Meta:
        db_table = "files"
        verbose_name = "files"
