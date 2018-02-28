from django.db import models

# Create your models here.

# Add new client.
class Client_Detail(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Add new Product like billing, Policies.
class Product_Area(models.Model):
    product_name = models.CharField(max_length=30)

    def __str__(self):
        return self.product_name

# Create new request for perticular client according request priority.
class Create_Request(models.Model):
    STATUS_CHOICES = (
                        ('Created', 'Created'),
                        ('In Progress', 'In Progress'),
                        ('Completed', 'Completed'),
                        ('Rejected', 'Rejected'),
                    )
    req_title = models.CharField(max_length=30)
    req_description = models.TextField()
    client_id  = models.ForeignKey(Client_Detail)
    pro_area_id  = models.ForeignKey(Product_Area)
    target_date = models.DateField()
    req_priority = models.IntegerField()
    status = models.CharField(max_length=40, choices=STATUS_CHOICES,default='Created')

    def __str__(self):
        return self.req_title        