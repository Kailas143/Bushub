from django.contrib import admin

from .models import Book, Bus, User

# Register your models here.

class BusAdmin(admin.ModelAdmin):
    list_display =['bus_name','src','dest','nos','rems','price','date','time']
    list_filter = ['src','dest']
    

admin.site.register(Bus,BusAdmin)
admin.site.register(Book)
admin.site.register(User)