# from django.shortcuts import render
# from .models import movie
# from django.http import JsonResponse
# # Create your views here.

# def movie_list(request):
#     movies = movie.objects.all()   # query set 
#     # print(movies.values())
#     data = {                             
#         "movies": list(movies.values())  # query set to python dictionary 
#     }
#     return JsonResponse(data)   # python dictionary to json response
    
# def movie_details(request,pk):
#     # global movie
#     movi = movie.objects.get(pk=pk)  # get movie by primary key
#     # print(movi)
#     data = {
#         'name ':movi.name,
#         'description': movi.description,
#         'active': movi.active
#     }
#     return JsonResponse(data)