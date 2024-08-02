from django.db import models
from .cases import Cases
from util.constants import ROLE_CHOICES

class PartiesInvolvedManager(models.Manager):
    def generate_id(self, case):
        last_record = self.filter(case = case).order_by('party_id').last()
        if not last_record:
            return case.case_id+'-P001'
        return case.case_id+f'-P{((int(last_record.party_id[10:])) + 1):03d}'

class PartiesInvolved(models.Model):
    party_id = models.CharField(max_length=15, null=True, unique=True)
    case = models.ForeignKey(Cases, null=False, on_delete=models.CASCADE)    
    role = models.CharField(max_length=30, null=False, choices=ROLE_CHOICES, default='petitioner')
    name = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    mobile_verified = models.BooleanField(default = False)
    email_verified = models.BooleanField(default = False)

    objects = PartiesInvolvedManager()
        
    class Meta:
        db_table = "parties_involved"
        verbose_name = "parties_involved"
