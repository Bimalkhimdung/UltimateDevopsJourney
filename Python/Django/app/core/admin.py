from django.contrib import admin

# including this here  adds model into admin

from .models import Core,Detail

# this shows Detail mode in same as user model 
class DetailsInline(admin.StackedInline):
    model = Detail


class CoreAdmin(admin.ModelAdmin):
    list_display = ("user_id","firstname", "lastname", "email")
    #this will order user by there user id and it must be list or tuple( separated by comma )
    inlines = [DetailsInline]
    ordering = ("user_id",)

admin.site.register(Core,CoreAdmin)


# this will show Detail model in separate
# class DetailAdmin(admin.ModelAdmin):
    # list_display = ("address","Phone_number",)
# admin.site.register(Detail,DetailAdmin)

