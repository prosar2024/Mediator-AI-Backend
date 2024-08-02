from django.db import models
from app.models.parties_involved import PartiesInvolved

class Conversations(models.Model):

    conversation_id = models.UUIDField(null=False, unique=True)
    updated_time = models.DateTimeField(null=False, auto_now_add=True)
    party = models.ForeignKey(PartiesInvolved, null=False, on_delete=models.CASCADE)    
    conversation = models.JSONField(null=True)
    closed = models.BooleanField(default = False)
    
    class Meta:
        db_table = "conversations"
        verbose_name = "conversations"
