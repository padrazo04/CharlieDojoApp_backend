from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import User, Belt, Lesson, ServiceDojoStudentBelt, Photo, ServiceDojo
#from tutorials.models import User, Belt, StudentBelt, Lesson
#from tutorials.serializers import UserSerializer, BeltSerializer, StudentBeltSerializer, LessonSerializer
from tutorials.serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView


# @api_view(['GET', 'POST', 'DELETE'])
# def tutorial_list(request):
#     # GET ALL TUTORIALS
#     if request.method == 'GET':
#         tutorials = Tutorial.objects.all()
        
#         title = request.GET.get('title', None)
#         if title is not None:
#             tutorials = tutorials.filter(title__icontains=title)
        
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)
#         # 'safe=False' for objects serialization
    
#     # CREATE AND SAVE A TUTORIAL
#     elif request.method == 'POST':
#         tutorial_data = JSONParser().parse(request)
#         tutorial_serializer = TutorialSerializer(data=tutorial_data)
#         if tutorial_serializer.is_valid():
#             tutorial_serializer.save()
#             return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # DELETE ALL TUTORIALS
#     elif request.method == 'DELETE':
#         count = Tutorial.objects.all().delete()
#         return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
# @api_view(['GET', 'PUT', 'DELETE'])
# def tutorial_detail(request, pk):
#     # find tutorial by pk (id)
#     try: 
#         tutorial = Tutorial.objects.get(pk=pk) 
#     except Tutorial.DoesNotExist: 
#         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
#     # GET A TUTORIAL GIVEN PK
#     if request.method == 'GET': 
#         tutorial_serializer = TutorialSerializer(tutorial) 
#         return JsonResponse(tutorial_serializer.data) 

#     # UPDATE A TUTORIAL GIVEN PK
#     elif request.method == 'PUT': 
#         tutorial_data = JSONParser().parse(request) 
#         tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
#         if tutorial_serializer.is_valid(): 
#             tutorial_serializer.save() 
#             return JsonResponse(tutorial_serializer.data) 
#         return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # DELETE A TUTORIAL GIVEN PK
#     elif request.method == 'DELETE': 
#         tutorial.delete() 
#         return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
# @api_view(['GET'])
# def tutorial_list_published(request):
#     tutorials = Tutorial.objects.filter(published=True)
        
#     if request.method == 'GET': 
#         tutorials_serializer = TutorialSerializer(tutorials, many=True)
#         return JsonResponse(tutorials_serializer.data, safe=False)


@api_view(['GET', 'PUT'])
def user_detail(request, pk):
    try: 
        user = User.objects.get(pk=pk) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET A TUTORIAL GIVEN PK
    if request.method == 'GET': 
        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data) 

    # UPDATE A TUTORIAL GIVEN PK
    elif request.method == 'PUT': 
        user_data = JSONParser().parse(request) 
        user_serializer = UserSerializer(user, data=user_data) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_detail_by_username(request, username):
    user = User.objects.filter(username=username)
        
    if request.method == 'GET': 
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)


'''
@api_view(['GET'])
def belts_list(request):
    belts = Belt.objects.all()
    nameBelt = request.GET.get('name', None)
    if nameBelt is not None:
        belts = belts.filter(title__icontains=name)
        
    if request.method == 'GET': 
        belts_serializer = BeltSerializer(belts, many=True)
        return JsonResponse(belts_serializer.data, safe=False)



'''
class Belts(APIView):
    def get(self, request, format=None):
    
        belts = Belt.objects.all()

        nameBelt = request.GET.get('name', None)
        if nameBelt is not None:
            belts = belts.filter(title__icontains=name)

        belts_serializer = BeltSerializer(belts, many=True)
        return JsonResponse(belts_serializer.data, safe=False)
            # 'safe=False' for objects serialization


class BeltsDetail(APIView):


    def get(self, request, pk):
    
        try: 
            belt = Belt.objects.get(pk=pk) 
        except Belt.DoesNotExist: 
            return JsonResponse({'message': 'The Belt does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        belts_serializer = BeltSerializer(belt) 
        return JsonResponse(belts_serializer.data) 

class StudentBelts(APIView):
    def get(self, request, format=None):

        studentBelts=ServiceDojoStudentBelt.objects.all()
        studentBelts_serializer=ServiceDojoStudentBeltSerializer(studentBelts, many=True)
        return JsonResponse(studentBelts_serializer.data, safe=False)


class StudentLesson(APIView):
    def get(self, request, **kwargs):
        #date = '2020-11-22'
        #service = 1
        #student = 1
        #date = self.query_params.get('date', None)
        service = self.kwargs.get('service', None)
        student = self.kwargs.get('student', None)
        date = self.kwargs.get('date', None)
        #lesson=Lesson.objects.raw("SELECT id FROM tutorials_lesson l WHERE ServiceDojo_id=any(SELECT ServiceDojo_id FROM tutorials_servicedojostudent WHERE student_id=1 ) AND date='2020-11-22'")
        #lesson=Lesson.objects.raw("SELECT id FROM tutorials_lesson l WHERE ServiceDojo_id=any(SELECT ServiceDojo_id FROM tutorials_servicedojostudent WHERE student_id=1 ) AND date='2020-11-22'")
        #lesson=Lesson.objects.raw("SELECT id FROM tutorials_lesson l WHERE ServiceDojo_id=(SELECT ServiceDojo_id FROM tutorials_servicedojostudent WHERE student_id=%s AND ServiceDojo_id=%s) AND date=%s", [student, service, date])
        lesson=Lesson.objects.raw("SELECT id FROM tutorials_lesson l WHERE ServiceDojo_id=(SELECT ServiceDojo_id FROM tutorials_servicedojostudent WHERE student_id=%s AND ServiceDojo_id=%s) AND date=%s", [student, service, date])
        lessons_serializer=LessonSerializer(lesson, many=True)
        return JsonResponse(lessons_serializer.data, safe=False)

    def post(self,request, format=None):

        StudentLesson_serializer = StudentLessonSerializer(data=request.data)
        if StudentLesson_serializer.is_valid():
            StudentLesson_serializer.save()
            return JsonResponse(StudentLesson_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(StudentLesson_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoStudent(APIView):
    def post(self, request, format=None):
        Photo_serializer = PhotoSerializer(data=request.data)
        if Photo_serializer.is_valid():
            Photo_serializer.save()
            return JsonResponse(Photo_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(Photo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def get(self, request, format=None):
    
        photos = Photo.objects.all()



        Photo_serializer = PhotoSerializer(photos, many=True)
        return JsonResponse(Photo_serializer.data, safe=False)
            # 'safe=False' for objects serialization

class ServiceDojoDetail(APIView):

    def get(self, request, pk):
        try: 
            service = ServiceDojo.objects.get(pk=pk) 
        except ServiceDojo.DoesNotExist: 
            return JsonResponse({'message': 'The Service does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        
        service_serializer = ServiceDojoSerializer(service) 
        return JsonResponse(service_serializer.data) 