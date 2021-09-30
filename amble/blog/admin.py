from django.contrib import admin
from .models import Blog, Blog_Reply, HashTag
# Register your models here.
admin.site.register(Blog)
admin.site.register(Blog_Reply)
admin.site.register(HashTag)