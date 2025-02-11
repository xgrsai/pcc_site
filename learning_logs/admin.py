from django.contrib import admin

from .models import Topic # Крапка перед models вказує Django шукати models.py в тому ж каталозі, що і admin.py

admin.site.register(Topic)
# Register your models here.
