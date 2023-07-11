from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=5000)
    price = models.IntegerField()
    ratings = models.IntegerField()
    reviews = models.IntegerField()
    overall_ratings = models.FloatField()
    link = models.TextField()
    img_link = models.TextField()
    prating = models.IntegerField()
    nrating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    query = models.CharField(max_length=5000, default="searchitem")

    def __str__(self):  
        return (self.product_name) 
    


