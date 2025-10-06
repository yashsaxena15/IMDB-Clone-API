from rest_framework.response import Response
from rest_framework import status,mixins,generics,viewsets,filters
from rest_framework.views import APIView
from watchlist_app.models import WatchList,StreamPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewListSerializer
from rest_framework.decorators import api_view 
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import BaseAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsReviewUserOrReadOnly,IsAdminOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
from watchlist_app.api.throtteling import ReviewListThrottle,CreateReviewThrottle
from django_filters.rest_framework import DjangoFilterBackend
from watchlist_app.api.pagination import WatchListPagination,WatchListLOPagination,WatchListCPagination

class UserReview(generics.ListAPIView):
    # queryset = Review.objects.all()
    
    serializer_class = ReviewListSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # def get_queryset(self):
    #     username = self.kwargs['username']
    #     return Review.objects.filter(review_user__username = username)
    
    def get_queryset(self):
        username = self.request.query_params.get('username',None)
        return Review.objects.filter(review_user__username=username) # for specifying review_user__username for username in review_user foreign field
    

# Create your views here.
# ModelViewSets - 

# class StreamPlatformVS(viewsets.ModelViewSet):  # for all operations 
    
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

class StreamPlatformVS(viewsets.ModelViewSet):  # for read only get for list and individual operations 
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# ViewSets and Routers - 

# class StreamPlatformVS(viewsets.ViewSet):  # we should not keep name same of ViewClass and modelClass
    
#     def list(self,request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset,many = True)
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk = None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset,pk = pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)


# Concreate view classes-

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [CreateReviewThrottle]
    # authentication_classes = [SessionAuthentication,BaseAuthentication] # thiss is the object level authentication
    def get_queryset(self):
        return Review.objects.all()
        
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user

    # Prevent multiple reviews by same user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this movie!")

    # Correct way to calculate running average
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating'])/2

        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, review_user=review_user)


        
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    
    serializer_class = ReviewListSerializer
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [ReviewListThrottle]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['review_user__username','active']
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['review_user__username','watchlist__title'] # if we have a foreign field of watchlist then we have to use __!
    filter_backends = [filters.OrderingFilter]
    search_fields = ['review_user__username','watchlist__title']

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    permission_classes = [IsReviewUserOrReadOnly]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-detail'
    
    
    
    
# class based views using mixins - 

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewListSerializer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args,**kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewListSerializer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)


# Class Based Views - 

# class StreamPlatformAV(APIView):
    
#     def get(self,request):
#         platforms = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(platforms,many = True,)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = StreamPlatformSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else : 
#             return Response(serializer.errors)

# class StreamPlatformDetailAV(APIView):
#     def get(self,request,pk):
#         try: 
#             movi = StreamPlatform.objects.get(pk=pk)
#         except  StreamPlatform.DoesNotExist:
#             return Response({'error':'not found'},status = status.HTTP_404_NOT_FOUND)

#         serializer = StreamPlatformSerializer(movi)
#         return Response(serializer.data)
#     def put(self,request,pk):
#         movi = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(movi,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         movi = StreamPlatform.objects.get(pk=pk)
#         movi.delete()
#         # return Response('Movie deleted successfully')
#         return Response(status=status.HTTP_204_NO_CONTENT)
class WatchListGV(generics.ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer 
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['avg_rating']

    # pagination_class = WatchListPagination
    # pagination_class = WatchListLOPagination
    pagination_class = WatchListCPagination
    
class WatchListAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    def get(self,request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WatchListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

class WatchDetailAV(APIView):
    
    permission_classes = [IsAdminOrReadOnly]

    def get(self,request,pk):
        try: 
            movi = WatchList.objects.get(pk=pk)
        except  WatchList.DoesNotExist:
            return Response({'error':'not found'},status = status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movi)
        return Response(serializer.data)
    def put(self,request,pk):
        movi = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movi,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        movi = WatchList.objects.get(pk=pk)
        movi.delete()
        # return Response('Movie deleted successfully')
        return Response(status=status.HTTP_204_NO_CONTENT) # when delete it will sent status code as NO CONTENT 


# Function Based Views - 

# @api_view(['GET','POST'])  # default GET Request method
# def movie_list(request):
#     if request.method == 'GET':
#         movies = movie.objects.all()   
#         serializer = movieserializer(movies,many = True)   # when we have multiple object, we need to define many = True
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = movieserializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else : 
#             return ResourceWarning(serializer.errors)
        
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try :
#             movi = movie.objects.get(pk=pk)
#         except movie.DoesNotExist:
#             return Response({'Error ':'Movie not found'}, status = status.HTTP_404_NOT_FOUND)
#         serializer = movieserializer(movi)
#         return Response(serializer.data)
#     if request.method == 'PUT': # in put we update every single field but in patch we only update the fields that are mentioned in the request
#         movi = movie.objects.get(pk=pk)
#         serializer = movieserializer(movi,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         movi = movie.objects.get(pk=pk)
#         movi.delete()
#         # return Response('Movie deleted successfully')
#         return Response(status=status.HTTP_204_NO_CONTENT) # when delete it will sent status code as NO CONTENT 