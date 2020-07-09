#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Local
from authenticator.models import Personal_data
from django.contrib.auth.models import User



@admin.register(Personal_data)
class authenticator_admin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'nationality', 'birth_date')
    list_display_links = ('pk',)
    list_editable = ('birth_date', 'user' )
    search_fields = ('user__email', 'user__first_name', 'user__last_name', )
    list_filter = ('created', 'modified')
    
    fieldsets = (
        ('Birth_data', {
            'fields': (('user','nationality', 'birth_date'),)
        }),
        ('Actual_data', {
            'fields': (('city', 'height', 'weigth'),),
        }),
        ('Meta_data', {
            'fields': (('created', 'modified',),),
        }),
    )
    
    readonly_fields = ('created', 'modified')

class Personal_dataInline(admin.StackedInline):
    model = Personal_data
    can_delete = False
    verbose_name_plural = 'Personal_data'

class UserAdmin(BaseUserAdmin):
    inlines = (Personal_dataInline,)
    list_display = (
        'username',
        'email',
        'first_name', 
        'last_name',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


