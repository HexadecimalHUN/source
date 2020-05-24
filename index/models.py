from django.db import models


class List(models.Model):
    objects = models.Manager()
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)


class AbstractBaseUser(models.Model):
    def get_username(self):
        return getattr(self, self.USERNAME_FIELD)
