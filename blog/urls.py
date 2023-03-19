from django.urls import path
from .views import *

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:art_id>/', PostSingle.as_view()),
    path('filter/', get_art_filter),
    path('comments/<int:art_id>/', AddComments.as_view(), name='add_comments'),
    path('<int:art_id>/like/', AddLike.as_view(), name='add_like'),
    path('<int:art_id>/del_like/', DelLike.as_view(), name='del_like'),
    path('search/', SearchView.as_view(), name='search_results'),
]