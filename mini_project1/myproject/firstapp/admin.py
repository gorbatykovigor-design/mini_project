from django.contrib import admin
from .models import Project, Skill, Expirience


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ['name']


class SkillAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ExpirienceAdmin(admin.ModelAdmin):
    list_display = ["position"]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Expirience, ExpirienceAdmin)
# Register your models here.
