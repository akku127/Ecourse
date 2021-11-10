from django.contrib import admin
from .models import Course, Category, LikeCourse, video, Comment

# Register your models here.

#
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug',)
#     prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course)
admin.site.register(Category)
admin.site.register(LikeCourse)
admin.site.register(video)
admin.site.register(Comment)