from django.contrib import admin

# Register your models here.
class ResortAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()