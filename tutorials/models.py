from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    completeName = models.CharField(max_length=70, default='')
    email= models.EmailField(max_length=255, unique=True)
    dni = models.CharField(max_length=9, blank=False, default='')
    dateofBirth = models.DateField(default='1901-01-01')
    phone = models.CharField(max_length=9, blank=False, default='')
    points = models.IntegerField(default=0)
    to_delete= models.BooleanField(default=False)

    #USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username +'  -  '+ self.dni


class Belt(models.Model):
    # ID fiels is added automatically
    name = models.CharField(max_length=70, blank=False, default='')
    photo = models.CharField(max_length=70, blank=False, default='')
    classesRequired = models.IntegerField(default=1)
    nextBelt = models.CharField(max_length=70, blank=False, default='')
    #students = models.ManyToManyField(User, through='StudentBelt')
    students = models.ManyToManyField(User, through='ServiceDojoStudentBelt')

    REQUIRED_FIELDS = [
        'name',
        'classesRequired',
    ]



    def __str__(self):
        return self.name

'''
class StudentBelt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)
    examDate = models.DateField()
    calification=models.CharField(max_length=25, default='no apto')
    attendedClasses=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    class Meta:
        unique_together=[['student', 'belt', 'examDate']]

    def __str__(self):
        return '%s -  %s (%s)' % (str(self.student), str(self.belt),self.calification)
'''

class ServiceDojo(models.Model):
    name= models.CharField(max_length=255, unique=True)
    serviceCost = models.FloatField(max_length=4, default=0)
    active = models.BooleanField(default=1)
    students = models.ManyToManyField(User, through='ServiceDojoStudent')

    #USERNAME_FIELD = 'username'

    def __str__(self):
        return '%s -  %s (%s)' % ((self.name), str(self.serviceCost),self.active)

class Lesson(models.Model):
    serviceDojo = models.ForeignKey(ServiceDojo, on_delete=models.CASCADE)
    #dateAndTime=models.DateTimeField()
    date=models.DateField(default='1901-01-01')
    Time=models.TimeField(default='00:00')

    duration=models.IntegerField(default=60)
    students = models.ManyToManyField(User, through='StudentLesson')

    def __str__(self):
        return '%s -  (%s)' % (str(self.date),self.serviceDojo)


class StudentLesson(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    assistance=models.BooleanField(default=False)

    class Meta:
        unique_together=[['student', 'lesson']]

    def __str__(self):
        return '%s -  %s (%s)' % (str(self.student), str(self.lesson),self.assistance)


class Photo(models.Model):
    photoPath=models.CharField(max_length=255)
    latitude=models.CharField(max_length=25)
    longitude=models.CharField(max_length=25)
    location=models.CharField(max_length=52)
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    validated = models.BooleanField(default=False)
    pointsForStudent = models.IntegerField(max_length=4, default=0)

    def __str__(self):
        return '%s -  %s' % (self.location, self.student)


class ServiceDojoStudent(models.Model):

    MONTH_TYPES = (
        (1, 'enero'), (2, 'febrero'),(3, 'marzo'),(4, 'abril'),(5, 'mayo'),(6,'junio'),
        (7, 'julio'), (8, 'agosto'),(9, 'septiembre'),(10, 'octubre'),(11, 'noviembre'),(12,'diciembre')
    )

    serviceDojo = models.ForeignKey(ServiceDojo, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    #month = models.IntegerField(  choices=MONTH_TYPES)# es preciso crear una entidad para el histórico de pagos
    #paid= models.BooleanField(default=False)

    class Meta:
        unique_together=[['serviceDojo', 'student']]

    def __str__(self):
        return '%s -  Student: %s ' % ((self.serviceDojo), (self.student) )

class ServiceDojoStudentBelt(models.Model):
    studentService = models.ForeignKey(ServiceDojoStudent, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    belt = models.ForeignKey(Belt, on_delete=models.CASCADE)
    examDate = models.DateField()
    calification=models.CharField(max_length=25, default='no apto')
    attendedClasses=models.IntegerField(default=0)
    active=models.BooleanField(default=True)
    class Meta:
        unique_together=[['studentService', 'belt', 'examDate']]

    def __str__(self):
        return '%s -  %s ' % (str(self.studentService), str(self.belt))

   

