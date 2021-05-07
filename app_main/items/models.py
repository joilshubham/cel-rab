from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, default='pending')
    item = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.item + str(self.id)
