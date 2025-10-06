from django.urls import path
# from watchlist_app.views import movie_list, movie_detail
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter
from django.urls import include

router = DefaultRouter()
router.register('platformlist',views.StreamPlatformVS,basename='platformlist')

            
urlpatterns = [
    
    path('watchlist/', views.WatchListAV.as_view(), name='watch_list'),
    path('watchlist2/', views.WatchListGV.as_view(), name='watch_list-test'),

    path('watchlist/<int:pk>/',views.WatchDetailAV.as_view(),name='watch_detail'),

    
    path('',include(router.urls)),
    # path('platformlist/',views.StreamPlatformAV.as_view(),name='platform_list'),
    # path('platformlist/<int:pk>/',views.StreamPlatformDetailAV.as_view(),name='platform_detail'),
    
    # path('review/',views.ReviewList.as_view(),name = 'review_list'),
    # path('review/<int:pk>/',views.ReviewDetail.as_view(),name='review_detail'),

    # path('platformlist/<int:pk>/review-create/',views.ReviewCreate.as_view(),name = 'review-create'),
    # path('platformlist/<int:pk>/review/',views.ReviewList.as_view(),name = 'review_list'),
    # path('platformlist/review/<int:pk>/',views.ReviewDetail.as_view(),name = 'review_detail'),

    path('<int:pk>/review-create/',views.ReviewCreate.as_view(),name = 'review-create'),
    path('<int:pk>/review/',views.ReviewList.as_view(),name = 'review_list'),
    path('review/<int:pk>/',views.ReviewDetail.as_view(),name = 'review_detail'),
    # path('reviews/<str:username>/',views.UserReview.as_view(),name = 'user-review_detail'),
    path('reviews/',views.UserReview.as_view(),name = 'user-review_detail'),



]
