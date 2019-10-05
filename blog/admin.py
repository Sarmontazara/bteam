from django.contrib import admin
from .models import Post,Order,Status

class OrderAdmin(admin.ModelAdmin):
    list_display=['name','email','date_created','price','zstatus','sale']
    ordering=['-date_created']

admin.site.register(Status)
admin.site.register(Post)
admin.site.register(Order,OrderAdmin)