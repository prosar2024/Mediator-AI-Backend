from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Cases, RelatedModel  # Replace RelatedModel with your actual related model

@receiver(pre_save, sender=Cases)
def prevent_update_if_closed(sender, instance, **kwargs):
    if instance.pk:  # Check if this is an update operation
        try:
            original = Cases.objects.get(pk=instance.pk)
            if original.closed_date is not None:
                raise ValidationError("Cannot update a case with a closed date.")
        except Cases.DoesNotExist:
            pass

@receiver(pre_save, sender=RelatedModel)
def prevent_related_update_if_closed(sender, instance, **kwargs):
    if instance.case and instance.case.closed_date is not None:
        raise ValidationError("Cannot update related record as the case is closed.")

@receiver(pre_delete, sender=Cases)
def prevent_delete_if_closed(sender, instance, **kwargs):
    if instance.closed_date is not None:
        raise ValidationError("Cannot delete a case with a closed date.")

@receiver(pre_delete, sender=RelatedModel)
def prevent_related_delete_if_closed(sender, instance, **kwargs):
    if instance.case and instance.case.closed_date is not None:
        raise ValidationError("Cannot delete related record as the case is closed.")
