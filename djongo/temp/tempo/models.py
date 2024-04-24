from djongo import models

class YourModel(models.Model):
    field1 = models.TextField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.TextField(max_length=100)

    def __str__(self):
        return self.field1


class OurModel(models.Model):
    field1 = models.TextField(max_length=100)
    field2 = models.IntegerField()

    def __str__(self):
        return self.field1