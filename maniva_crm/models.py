from djongo import models


class Customer(models.Model):
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
    SERVICE_CHOICES = (
        ("Digital Development & Optimization", "Digital Development & Optimization"),
        ("Strategic Business Review", "Strategic Business Review"),
        ("Creating Customer Value", "Creating Customer Value"),
    )
    name = models.CharField(max_length=200, null=True, choices=SERVICE_CHOICES)
    price = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    date_created = date_created = models.DateTimeField(auto_now_add=True, null=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Could Not Complete Transaction", "Could Not Complete Transaction"),
        ("Transaction Completed", "Transaction Completed"),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    service = models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.service.name
