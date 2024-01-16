from django.contrib import admin

from personality_test.models import Choice, Question
# Register your models here.

admin.site.register(Choice)
admin.site.register(Question)