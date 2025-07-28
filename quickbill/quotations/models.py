from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quotation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_name = models.CharField( max_length=100)
    client_email = models.EmailField()
    project_title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Quotation for {self.client_name} - {self.project_title}"