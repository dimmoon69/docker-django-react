from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()
admin.site.empty_value_display = '--Пусто--'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_superuser')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
