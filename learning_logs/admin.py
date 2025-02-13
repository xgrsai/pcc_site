from django.contrib import admin

from .models import Topic, Entry # Крапка перед models вказує Django шукати models.py в тому ж каталозі, що і admin.py

admin.site.register(Topic)
admin.site.register(Entry)

