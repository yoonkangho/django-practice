# built-in imports
from datetime import datetime

# third party imports
from django.db import models

# application imports


class BaseManager(models.Manager):
    def get_query_set(self):
        return super().get_query_set().filter(deleted_at__isnull=True)


class BaseModel:
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        force_delete = kwargs.pop("force", False)
        if force_delete:
            super().delete(**kwargs)
        else:
            model = self.__class__
            kwargs.update({"deleted_at": datetime.now()})
            model.objects.filter(pk=self.pk).update(**kwargs)
