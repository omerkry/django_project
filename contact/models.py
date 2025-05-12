from django.db import models

class GeneralSetting(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)
    description = models.CharField(max_length=255, default='', blank=True)
    parameter = models.CharField(max_length=255, default='', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

class ImportSetting(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)
    description = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.name

class ImageSetting(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)
    description = models.CharField(max_length=255, default='', blank=True)
    file = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} at {self.company}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, blank=True, help_text="Örn: fa fa-html5")
    level = models.IntegerField(default=0, help_text="0-100 arası beceri seviyesi")

    def __str__(self):
        return self.name

# ✅ EKLENEN: Education Modeli
class Education(models.Model):
    school = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.school} - {self.degree}"
