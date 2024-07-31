from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from models.models import Comment
from models.serializers import CommentSerializer


@api_view(['GET'])
def comments_list(request, post_id):
    if request.method == 'GET':
        comments = Comment.objects.filter(post_id=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    


@api_view(['POST'])
# @permission_classes([IsEmployer, IsAuthenticated])
def new_comment(request):
    if request.method == 'POST':
        comment_data = {
            'comment': request.data.get('comment'),
            'created_by': request.user.id,
            'post': request.data.get('post_id')
        }

        serializer = CommentSerializer(data=comment_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"comment": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error": "Only POST method is allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)