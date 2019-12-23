from django.contrib import admin
from .models import Samsung, Phone, Apple


# Register your models here
class SamsungAdmin(admin.ModelAdmin):
    pass
class PhoneAdmin(admin.ModelAdmin):
    pass
class AplleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Samsung, SamsungAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Apple, PhoneAdmin)
