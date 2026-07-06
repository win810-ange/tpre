from django.contrib import admin
from .models import Discussion
from user.models import User
from signalement.models import Signalement
# Register your models here.




admin.site.register(Discussion)

admin.site.register(User)



@admin.register(Signalement)
class GenererSignalement(admin.ModelAdmin):
    list_display = ('type', 'localisation')

