from django.contrib import admin
from .models import Topping_type, Standard_pizza, Sicilian_pizza, Sub, Pasta, Salad, Platter, Topping, Orders_tracking, Orders_list

# Register your models here.
admin.site.register(Sicilian_pizza)
admin.site.register(Standard_pizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)
admin.site.register(Topping)
admin.site.register(Orders_tracking)
admin.site.register(Orders_list)





