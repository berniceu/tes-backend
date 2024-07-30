from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from models.models import Post
from models.serializers import PostSerializer



@api_view(['GET'])
def posts_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data}, status=status.HTTP_200_OK)
    


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def new_post(request):
    if request.method == 'POST':
        post_data = {
            'name': request.data.get('name'),
            'content': request.data.get('content'),
            'created_by': request.user.id
        }

        serializer = PostSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"post": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "Only POST method is allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)