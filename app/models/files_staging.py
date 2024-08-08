from django.db import models
from .conversation_staging import ConversationStaging

class FilesStaging(models.Model):
    file_id = models.UUIDField(null=False, unique=True)
    conversation_staging = models.ForeignKey(ConversationStaging, null=True, on_delete=models.CASCADE)    
    unique_file_name = models.CharField(max_length=200, null=True)
    actual_file_name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=4000, null=True) 
    
    class Meta:
        db_table = "files_staging"
        verbose_name = "files_staging"
