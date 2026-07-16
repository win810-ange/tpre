from django.contrib import admin
from .models import Discussion, Reponse
from user.models import User
from django.utils.html import format_html
from signalement.models import Signalement
# Register your models here.




admin.site.register(Discussion)

admin.site.register(Reponse)

admin.site.register(User)



@admin.register(Signalement)
class GenererSignalement(admin.ModelAdmin):
    readonly_fields = ("apercu_image",)
    def apercu_image(self, obj):
        if obj.image :
            return format_html(
                '<img src="{}" width="150" />', obj.image.url
            )
        else :
            return "Aucune image"

    apercu_image.short_description = "Aperçu"