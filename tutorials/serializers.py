from rest_framework import serializers 
#from tutorials.models import User, Belt, StudentBelt, Lesson, StudentLesson, Photo, ServiceDojoStudentBelt
from tutorials.models import *
 

 
class BeltSerializer(serializers.ModelSerializer):
 
    users = serializers.SerializerMethodField()
    userServive=serializers.SerializerMethodField()

    class Meta:
        model = Belt
        fields = ('id',
                'name',
                'photo',
                'classesRequired',
                'nextBelt',
                'users',
                'userServive')         
       #read_only_fields=('id')

    def get_users(self, belt):
        query_datas = ServiceDojoStudentBelt.objects.filter(belt=belt)
        return [ServiceDojoStudentBeltSerializer(student).data for student in query_datas]

    def get_userServive(self, belt):
        query_datas2 = ServiceDojoStudentBelt.objects.filter(belt=belt)
        return [ServiceDojoStudentBeltSerializer(studentService).data for studentService in query_datas2]



class UserSerializer(serializers.ModelSerializer):
    
    belts = serializers.SerializerMethodField()
    lessons=serializers.SerializerMethodField()
    photos=serializers.SerializerMethodField()

    class Meta:
      model = User
      #fields = ('id', 'username','belts','lessons')
      fields = ('__all__')
      depth = 3

    def get_lessons(self, student):
        query_datas1 = StudentLesson.objects.filter(student=student)
        return [StudentLessonSerializer(lesson).data for lesson in query_datas1]

    def get_photos(self, student):
        query_datas2 = Photo.objects.filter(student=student)
        return [PhotoSerializer(photo).data for photo in query_datas2]

    def get_belts(self, student):
        query_datas3 = ServiceDojoStudentBelt.objects.filter(student=student)
        return [ServiceDojoStudentBeltSerializer(belt).data for belt in query_datas3]



'''

class StudentBeltSerializer(serializers.ModelSerializer):
'''
#student=UserSerializer(many=True, read_only=False)
#student_id = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(), source='user')
#student_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=User.objects.all(), source='student')
#belt=BeltSerializer(many=True, read_only=False)
#belt_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Belt.objects.all(), source='belt')
'''

class Meta:
model = StudentBelt
fields = ('__all__')

def create(self, validated_data):
student = validated_data.pop('student_id')
belt = validated_data.pop('belt_id')
student_belt = StudentBelt.objects.create(student=student_id,**validated_data)
for tg in belt:
    student_belt.belt.add(tg)
return student_belt
'''

class StudentLessonSerializer(serializers.ModelSerializer):
    '''
    student=UserSerializer(many=True, read_only=False)
    #student_id = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=User.objects.all(), source='user')
    student_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=User.objects.all(), source='student')
    belt=BeltSerializer(many=True, read_only=False)
    belt_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Belt.objects.all(), source='belt')
    '''
    lessons=serializers.SerializerMethodField()

    class Meta:
       model = StudentLesson
       fields = ('__all__')

    def get_lessons(self, studentlesson):
        query_datas1 = Lesson.objects.filter(studentlesson=studentlesson)
        return [LessonSerializer(lesson).data for lesson in query_datas1]

    '''
    def create(self, validated_data):
        student = validated_data.pop('student_id')
        belt = validated_data.pop('belt_id')
        student_belt = StudentBelt.objects.create(student=student_id,**validated_data)
        for tg in belt:
            student_belt.belt.add(tg)
        return student_belt
      
         #read_only_fields=('id', 'student', 'belt')
    '''

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
       model = Photo
       fields = ('__all__')


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
       model = Lesson
       fields = ('__all__')


class StudentLessonSerializer(serializers.ModelSerializer):

    class Meta:
       model = StudentLesson
       fields = ('__all__')



class ServiceDojoStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceDojoStudent
        fields = ('__all__')


class ServiceDojoStudentBeltSerializer(serializers.ModelSerializer):

    studentService=serializers.SerializerMethodField()
    #student=serializers.SerializerMethodField()
    depth = 4

    class Meta:
        model = ServiceDojoStudentBelt
        fields = ('__all__')

    def create(self, validated_data):
        studentService = validated_data.pop('servicedojostudent_id')
        belt = validated_data.pop('belt_id')
        studentservice_belt = ServiceDojoStudentBelt.objects.create(student=studentservice_id,**validated_data)
        for tg in belt:
            studentservice_belt.belt.add(tg)
        return studentservice_belt

    def get_studentService(self, servicedojostudentbelt):
        query_datas1 = ServiceDojoStudent.objects.filter(servicedojostudentbelt=servicedojostudentbelt)
        return [ServiceDojoStudentSerializer(ServiceDojoStudent).data for ServiceDojoStudent in query_datas1]
    '''
    def get_student(self, student):
        query_datas2 = User.objects.filter(id=student)
        return [UserSerializer(user).data for (user) in query_datas2]
    '''


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('__all__')


class ServiceDojoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceDojo
        fields = ('__all__')
           