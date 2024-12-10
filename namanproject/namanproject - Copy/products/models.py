from django.db import models

# Create your models here.
class Product (models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.PositiveBigIntegerField()
    created_at= models.DateTimeField()

    def __str__(self):
        return self.name
    
    class Meta:
        # Adding database indexes for category and price fields
        indexes = [
            models.Index(fields=['category']),  # Index for category
            models.Index(fields=['price']),     # Index for price
        ]