from django.contrib import admin
from app.models import Students,Subjects,iaMarks,ClassStudents
# Register your models here.
admin.site.register(Students)
admin.site.register(Subjects)
admin.site.register(ClassStudents)
admin.site.register(iaMarks)
