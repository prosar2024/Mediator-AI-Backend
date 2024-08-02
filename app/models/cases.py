from django.db import models
from .mediators import Mediators

class CasesManager(models.Manager):
    def generate_id(self):
        last_record = self.all().order_by('case_id').last()
        if not last_record:
            return 'C0000001'
        return f'C{((int(last_record.case_id[1:])) + 1):07d}'

class Cases(models.Model):

    case_id = models.CharField(max_length=20, null=False, unique=True)
    created_on = models.DateTimeField(null=False, auto_now_add=True)
    summary = models.CharField(max_length=5000, null=True)
    
    mediator = models.ForeignKey(Mediators, null=False, on_delete=models.CASCADE)
    closed_on = models.DateTimeField(null=True)
    
    objects = CasesManager()

    class Meta:
        db_table = "cases"
        verbose_name = "cases"
    