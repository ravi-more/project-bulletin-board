from django.contrib import admin

# Register your models here.

# from .models import Post

from .models import Projectinfo, links

# admin.site.register(Post)

admin.site.register(Projectinfo)
admin.site.register(links)
