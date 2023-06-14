from django.contrib import admin

# Register your models here.

from store.models import Game
from store.models import Platform
from store.models import Category
from store.models import Key

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Category)
admin.site.register(Key)
