from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import Course
from .serializers import CourseSerializer

from django.apps import apps

# Create your views here.


def get_years(request, pk):
  courses = Course.objects.get(pk=pk)
  years_list = courses.filter(year=courses.course.purchase_date)


#<<<<<<<<< GET / Retrieve >>>>>>>>>>
#--Done-- Get all courses (Courses Main Page)
#--Done-- Get course details (Course detail Page)
#         Get Top 3 Courses (Home page-dashboard)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_all_courses(request):
  courses = Course.objects.filter(user_id=request.user.id)
  #courses = Course.objects.filter(user__id = pk)
  serializer = CourseSerializer(courses, many=True)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def view_course_detail(request, pk):
    try:
      course = Course.objects.get(pk=pk) 
    except Course.DoesNotExist:
      raise Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CourseSerializer(course)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated]) 
def view_top_courses(request):
  pass


#<<<<<<<<< POST / Create >>>>>>>>>>
#--Done--  Create new course ( Course form module)

@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def add_course(request):
  serializer = CourseSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save(user = request.user)   #Does something go in the argument?
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#<<<<<<<<< PUT / Update >>>>>>>>>>
#         Update course info (Course detail page > Update course form module)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_course(request, pk):
  try:
    course = Course.objects.get(pk=pk)
  except Course.DoesNotExist:
    raise Response(status=status.HTTP_404_NOT_FOUND)
  serializer = CourseSerializer(course, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#<<<<<<<<< DELETE / Delete >>>>>>>>>>
#         Delete course (Course detail page > Delete form warning module)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_course(request, pk):
  course = Course.objects.get(pk=pk)
  course.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)


#<<<<<<<<< Fetch Chart Data >>>>>>>>>>
#         

# @api_view([''])
# @permission_classes([IsAuthenticated])
# def yearly_courses(request, user_id):
#   yearlyTotal = apps.get_model('courses.Course')

#1. Get the year from the Purchase date column (x column label)
#2. Add all of the prices together
#3. Make the year with the highest amount be the max on the y-axis
#4. Have the y-axis units be by 1000 dollars
#5. 


# <<<<<<<<<<<<<<<<< Notes <<<<<<<<<<<<<<<<<

# (@ 6:03 ) VIEWS: React Django Starter Code - Backend Walkthrough


# @api_view(['GET'])
# @permission_classes([AllowAny]) #Change to IsAuthenticated?
# def get_all_courses(request):
#     courses = Course.objects.all()
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def user_courses(request):
#     print(
#       'User ', f"{request.user.id} {request.user.email} {request.user.username}")
#     if request.method == 'POST':
#       serializer = CourseSerializer(data=request.data)
#       if serializer.is_valid():
#         serializer.save(user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#       elif request.method == 'GET':
#         courses = Course.objects.filter(user_id=request.user.id)
#         serializer = CourseSerializer(courses, many=True)
#         return Response(serializer.data)