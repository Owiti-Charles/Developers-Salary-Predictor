from django.db import models


class DeveloperSurvey(models.Model):
    dev_type = models.CharField(max_length=100, blank=True)
    years_code_pro = models.FloatField(null=True, blank=True)
    years_of_coding = models.FloatField(null=True, blank=True)
    converted_comp_yearly = models.FloatField(null=True, blank=True)
    ed_level = models.CharField(max_length=100, blank=True)
    countries = models.TextField(blank=True)
    programming_languages = models.TextField(blank=True)
    ai_select = models.CharField(max_length=50, choices=[
        ('Yes', 'Using AI'),
        ('No, but I plan to soon', 'Planning to Use AI'),
        ('No', 'Not Using AI')
    ], blank=True)
    industry = models.CharField(max_length=100, blank=True)
    platforms = models.TextField(blank=True)
    remote_work = models.CharField(max_length=50, )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dev_type} - {self.created_at}"

