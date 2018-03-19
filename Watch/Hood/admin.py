from django.contrib import admin
from .models import Business,User_profile,Neigbourhood,Post

# Register your models here.

admin.site.register(Business)
admin.site.register(User_profile)
admin.site.register(Neigbourhood)
admin.site.register(Post)

