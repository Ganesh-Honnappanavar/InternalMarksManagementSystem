from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
Gender=(
('MALE','MALE'),
('FEMALE','FEMALE'),
)

class Students(models.Model):
    USN          = models.CharField(primary_key=True,max_length=15)
    StudentName  = models.CharField(max_length=15)
    Address  = models.CharField(max_length=25)
    phone  = models.IntegerField(max_length=10)
    Gender  = models.CharField(max_length=6,choices=Gender)

    def __str__(self):
        return '%s %s' %(self.USN,self.StudentName)

sem=(
('1','1'),
('2','2'),
('3','3'),
('4','4'),
('5','5'),
('6','6'),
('7','7'),
('8','8'),
)

class ClassStudents(models.Model):
    USN_1  = models.ForeignKey(Students,on_delete=models.CASCADE)
    SEM  = models.CharField(max_length=1,choices=sem)

    def __str__(self):
        return '%sth SEM %s' %(self.SEM,self.USN_1)

class Subjects(models.Model):
    subcode = models.CharField(primary_key=True,max_length=7)
    title  = models.CharField(max_length=25)
    SEM  = models.CharField(max_length=1,choices=sem)
    owner       = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return '%s %s Assigned to Prof. %s' %(self.subcode,self.title,self.owner)


    class Meta:
        verbose_name_plural='Staff Assignment'


class iaMarks(models.Model):
    usnIA   = models.ForeignKey(Students,on_delete=models.CASCADE)
    sub_code   = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    SEM  = models.CharField(max_length=1,choices=sem)
    t1    = models.PositiveIntegerField(validators=[MaxValueValidator(15),MinValueValidator(0)])
    t2    = models.PositiveIntegerField(validators=[MaxValueValidator(15),MinValueValidator(0)])
    t3    = models.PositiveIntegerField(validators=[MaxValueValidator(15),MinValueValidator(0)])

    def average(self):
        if self.t1>=self.t2>=self.t3:
            self.avg=(self.t1+self.t2)/2
        elif self.t2>=self.t3>=self.t1:
            self.avg=(self.t2+self.t3)/2
        else:
            self.avg=(self.t3+self.t1)/2
        return self.avg





    def __str__(self):
        return '%s Test marks of %s is %s, %s, %s' %(self.usnIA,self.sub_code,self.t1,self.t2,self.t3)

class staff(models.Model):
    staffId = models.IntegerField()
    staff_name = models.CharField(max_length=15)
    Gender  = models.CharField(max_length=6,choices=Gender)


    def __str__(self):
        return '%s %s' %(self.staffId,self.staff_name)


