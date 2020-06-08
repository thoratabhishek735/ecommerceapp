from django.contrib import admin

# Register your models here.
from .models import product
admin.site.register(product)

from .models import prodw
admin.site.register(prodw)

from .models import Contact
admin.site.register(Contact)

from .models import Orders
admin.site.register(Orders)


from .models import OrderUpdate
admin.site.register(OrderUpdate)
