from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from models.models import *
from models.serializers import *


@api_view(['GET'])
def courses_list(request):
        if request.method == 'GET':
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response({"courses": serializer.data}, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def course_detail(request, id):
    try:
        course = Course.objects.get(pk=id)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course)
    return Response({"course": serializer.data}, status=status.HTTP_200_OK)



@api_view(['POST'])
# @permission_classes([IsEmployer, IsAuthenticated])
def new_course(request):
    if request.method == 'POST':
        course_data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'source_link': request.data.get('source_link'),
            'level': request.data.get('level'),
            'hours': request.data.get('hours'),
            'lessons': request.data.get('lessons'),
            'exercises': request.data.get('exercises'),
            'projects': request.data.get('projects'),
            'skills': request.data.get('skills', []),
            
        }

        serializer = CourseSerializer(data=course_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"course": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Only POST method is allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
