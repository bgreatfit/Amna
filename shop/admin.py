from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Featured_Ads)
admin.site.register(count_down_ads)
admin.site.register(Main_Category)
admin.site.register(Characteristics)
admin.site.register(Products_Additional_Pictures)
admin.site.register(site_settings)
admin.site.register(order)