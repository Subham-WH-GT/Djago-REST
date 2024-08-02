from django.contrib import admin
from .models import PlayerModel

# admin.site.register(PlayerModel)
@admin.register(PlayerModel)
class PlayerModelAdmin(admin.ModelAdmin):
    list_display=['id','playerName','jerseyNumber','country']

# Register your models here.
