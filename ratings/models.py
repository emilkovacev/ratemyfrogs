from django.db import models

class Frog(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=1000)
    total = models.PositiveIntegerField(default=0)
    n = models.PositiveIntegerField(default=0)

    @property
    def avg(self):
        if self.n > 0:
            return self.total / self.n
        return 0

    def __str__(self):
        return str(self.title)


class User(models.Model):
    user_id = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.userid)

