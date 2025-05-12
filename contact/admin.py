from django.contrib import admin
from contact.models import GeneralSetting, ImportSetting, ImageSetting, Experience, Skill, Education

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parameter', 'created_date', 'updated_date')
    search_fields = ('name', 'description')

@admin.register(ImportSetting)
class ImportSettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'preview', 'created_date', 'updated_date')
    search_fields = ('name',)

    def preview(self, obj):
        if obj.file:
            return f'<img src="{obj.file.url}" width="50" height="50" style="object-fit: cover;" />'
        return "(No Image)"
    preview.allow_tags = True
    preview.short_description = 'Preview'

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'start_date', 'end_date')
    search_fields = ('title', 'company', 'location')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class', 'level')
    search_fields = ('name', 'icon_class')

# ✅ EKLENEN: Education admin kaydı
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school', 'degree', 'department', 'start_year', 'end_year')
    search_fields = ('school', 'degree', 'department')
