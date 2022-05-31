from django.contrib import admin
from .models import RamenCorner

class RamenCornerAdmin(admin.ModelAdmin):
    list = ('title', 'videoUrl')

admin.site.register(RamenCorner, RamenCornerAdmin)


