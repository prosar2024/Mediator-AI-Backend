from django.db import models

class ConversationStaging(models.Model):

    conversation_id = models.UUIDField(null=False, unique=True)
    system_fingerprint = models.UUIDField(null=False, unique=False)
    start_date = models.DateTimeField(null=False, auto_now_add=True)
    conversation = models.JSONField(null=True)
    
    class Meta:
        db_table = "conversations_staging"
        verbose_name = "conversations_staging"
