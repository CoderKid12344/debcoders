from django.contrib import admin
from home.models import Blog, Contact

# Register your models here.
admin.site.register(Contact)

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     class Media:
#         js = ('js/tinyinject.js',)
admin.site.register(Blog)