from django.contrib import admin
from .models import Year,Semester,Book,Other

a=[Year,Semester,Book,Other]
for i in a:
	admin.site.register(i)

# Register your models here.
