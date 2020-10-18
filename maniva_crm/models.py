from djongo import models


class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.name


class Service(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Could Not Complete Transaction", "Could Not Complete Transaction"),
        ("Transaction Completed", "Transaction Completed"),
    )

    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.product.name
