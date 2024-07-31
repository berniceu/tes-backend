from django.urls import path
from api.views.comments.comments import comments_list, new_comment
from api.views.courses.courses import courses_list, new_course, course_detail
from api.views.posts.posts import posts_list, new_post, post_detail


urlpatterns = [
    path('posts/<int:post_id>/comments/', comments_list, name='comments_list'),
    path('courses/', courses_list, name='courses_list'),
    path('courses/<int:id>/', course_detail, name='course_detail'),
    path('posts/', posts_list, name='posts_list'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('posts/new_post/', new_post, name='new_post'),
    path('posts/new_course', new_course, name='new_course'),
    path('posts/<int:post_id>/new_comment/', new_comment, name='new_comment'),
]