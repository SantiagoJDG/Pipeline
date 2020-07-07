#Django
from django.contrib import admin

#Local
from authenticator.models import Personal_data

@admin.register(Personal_data)
class authenticator_admin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'nationality', 'birth_date')
    list_display_links = ('pk', 'user')
    list_editable = ('birth_date', )
    search_fields = ('user__email', 'user__first_name', 'user__last_name', )
    list_filter = ('created', 'modified')
    


# Register your models here.
