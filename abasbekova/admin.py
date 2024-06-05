from django.contrib import admin
from .models import addcard
# Register your models here.
@admin.register(addcard)
class adminCard(admin.ModelAdmin):
    list_display = ['title', 'text', 'image']