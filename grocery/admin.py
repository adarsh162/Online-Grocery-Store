from itertools import product
from unicodedata import category
from django.contrib import admin

from grocery.models import products


# Register your models here.
admin.site.register(products)

