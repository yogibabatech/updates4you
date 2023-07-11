from django.forms import ModelForm, fields
from models import Product

class Productlist(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'ratings', 'reviews', 'overall_ratings', 'link', 'img_link']

        

