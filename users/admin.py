from django.contrib import admin

from users.models import User
from products.admin import BasketAdmin





@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','get_groups')
    search_fields = ('username','email')
    inlines = (BasketAdmin,)


    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Группы'



