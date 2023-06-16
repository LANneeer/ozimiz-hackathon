from django.contrib import admin
from courses.models import Material, Course, CourseCompletion

admin.site.register(Material)
admin.site.register(Course)
admin.site.register(CourseCompletion)
