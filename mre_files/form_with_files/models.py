from django.db import models
from django.forms import ValidationError


class ModelWithFileField(models.Model):
    first_image_title = models.CharField(max_length=100)
    file_field = models.FileField(upload_to='uploads/', null=True, blank=True)
    second_file_field = models.FileField(upload_to='uploads/', null=True, blank=True)

    def clean(self):
        if self.first_image_title:
            if not self.file_field:
                raise ValidationError({
                    'file_field': (
                        "You must upload a file if you have a title.")
                    })
        return super().clean()