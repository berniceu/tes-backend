from django.urls import path
from api.views.comments.comments import comments_list, new_comment
from api.views.courses.courses import courses_list, new_course
from api.views.posts.posts import posts_list, new_post


urlpatterns = [
    path('comments/', comments_list, name='comments_list'),
    path('courses/', courses_list, name='courses_list'),
    path('posts/', posts_list, name='posts_list'),
    path('posts/new_post/', new_post, name='new_post'),
    path('posts/new_course', new_course, name='new_course'),
    path('posts/new_comment', new_comment, name='new_comment'),
]