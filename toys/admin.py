from django.contrib import admin
from .models import Material, Toy

admin.site.register(Toy)
admin.site.register(Material)

admin.site.site_title = 'Dariana Toys'
admin.site.site_header = "DarianaToys"