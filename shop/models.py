from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

# Create your models here.

class order(models.Model):
    first_name = models.CharField(max_length=250,blank=True,null=True)
    last_name = models.CharField(max_length=250,blank=True,null=True)
    company = models.CharField(max_length=250,blank=True,null=True)
    country = models.CharField(max_length=250,blank=True,null=True)
    street_address1 = models.CharField(max_length=250,blank=True,null=True)
    street_address2 = models.CharField(max_length=250,blank=True,null=True)
    city = models.CharField(max_length=250,blank=True,null=True)
    state = models.CharField(max_length=250,blank=True,null=True)
    phone_number = models.CharField(max_length=250,blank=True,null=True)
    email_address = models.CharField(max_length=250,blank=True,null=True)
    note = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    products = models.ManyToManyField('Product',related_name="Orderd_products")
    date_time =  models.DateTimeField(default=timezone.now)
    price = models.IntegerField(default=0,null=True)
    processing = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    




class Main_Category(models.Model):
    name = models.CharField(max_length=250,blank=True)
    categories = models.ManyToManyField('Category')


class Category(models.Model):
    name = models.CharField(max_length=250,blank=True)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to="categories", blank=True)
    description = models.TextField(blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to="products", blank=True)
    brand = models.CharField(max_length=250, blank=True)
    shipping = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True)
    featured = models.BooleanField(default=False,blank=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    short_description = models.TextField(blank=True)
    review = models.ForeignKey('Review', on_delete=models.CASCADE,blank=True,null=True)
    characteristics = models.ManyToManyField('Characteristics')
    additional_images = models.ManyToManyField('Products_Additional_Pictures')


    def __str__(self):
        return self.name

class Products_Additional_Pictures(models.Model):
    image = models.ImageField(upload_to="products", blank=True)



class Characteristics(models.Model):
    Character = models.CharField(max_length=255,blank=True,null=True)
    
    def __str__(self):
        return self.Character
    



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    rate = models.IntegerField(default=10, validators=[MaxValueValidator(10), MinValueValidator(1)])
    review = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    active = models.BooleanField(default=True,null=True)

    def __str__(self):
        return self.review


class Featured_Ads(models.Model):
    name = models.CharField(max_length=250, null=True,blank=True)
    image = models.ImageField(upload_to="ads", blank=True)
    percent_off_deal = models.CharField(max_length=255, null=True,blank=True)

class count_down_ads(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    main_image_slide1 = models.ImageField(upload_to="ads", blank=True, help_text="image size must be : 321 x 450")
    main_image_slide2 = models.ImageField(upload_to="ads", blank=True, help_text="image size must be : 321 x 450")
    main_image_slide3 = models.ImageField(upload_to="ads", blank=True, help_text="image size must be : 321 x 450")
    img_1 = models.ImageField(upload_to="ads", blank=True, help_text="image size must be : 123 x 127")
    img_2 = models.ImageField(upload_to="ads", blank=True, help_text="image size must be : 123 x 127")
    img_3 = models.ImageField(upload_to="ads", blank=True, help_text="image size must be : 123 x 127")
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    description = models.TextField(blank=True,null=True)
    count_down_date = models.CharField(max_length=255, null=True,blank=True,help_text="e.g: 2022/10/01")


# class Landing_products(models.Model):
#     name = models.CharField(max_length=255,null=True,blank=True)
#     image = models.ImageField(upload_to="logo", blank=True)
#     image_two = models.ImageField(upload_to="logo", blank=True)
#     short_description = models.TextField(blank=True,null=True)



class site_settings(models.Model):
    site_name = models.CharField(max_length=255,null=True,blank=True)
    logo = models.ImageField(upload_to="logo", blank=True)
    phone_number = models.CharField(max_length=250, null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)

#class mega_sale(models.Model):
#     name = models.CharField(max_length=255,null=True,blank=True)
#     main_image_slide1 = models.ImageField(upload_to="ads", blank=True, help_text="image size must be : 500 x 575")
#     main_image_slide2 = models.ImageField(upload_to="ads", blank=True, help_text="image size must be : 321 x 450")










