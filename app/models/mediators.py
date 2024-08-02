from django.db import models

class MediatorsManager(models.Manager):
    def generate_id(self):
        last_record = self.all().order_by('mediator_id').last()
        if not last_record:
            return 'M10001'
        return f'M{((int(last_record.mediator_id[1:])) + 1):05d}'

class Mediators(models.Model):

    mediator_id = models.CharField(max_length=5,null=False, unique=True)
    name = models.CharField(max_length=30, null=False)
    mobile = models.CharField(max_length=10, null=False)
    email = models.EmailField(null=False)
    mobile_verified = models.BooleanField(default = False)
    email_verified = models.BooleanField(default = False)

    objects = MediatorsManager()

    class Meta:
        db_table = "mediators"
        verbose_name = "mediators"
    
    