from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review

# models.serializers 

class ReviewListSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    class Meta : 
        model = Review
        exclude = ['watchlist']
        # fields = "__all__"
        


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewListSerializer(many = True, read_only = True)
    # len_name = serializers.SerializerMethodField() # this is used to create a new field without adding in models
    platform = serializers.CharField(source = 'platform.name')
    class Meta :
        model = WatchList 
        fields = "__all__"
        # fields = ['name','description','active'] # which want to include
        # exclude = ['id']  # which one wants to exclude 
        
class StreamPlatformSerializer(serializers.ModelSerializer):
# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many = True, read_only = True) # this watchlist variable name should be related_name in models.py file
    # platform = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='streamplatform_detail',  # <-- match your urls.py
    #     lookup_field = "pk",

    # )

    # watchlist = serializers.StringRelatedField(many=True) # this will display all string related fields in model
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name = 'watch_detail'
    # )   # this will be used for redirecting that actual detail or create a link

    class Meta :
        model = StreamPlatform
        fields = "__all__"


    # def get_len_name(self,object): 
    #     return len(object.name)
    # def validate_name(self,value):  # field level validation 
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value
    
    # def validate(self,value): # object level validation
    #     if value['name'] == value['description']:
    #         raise serializers.ValidationError("Name and description should be different")
    #     else : 
    #         return value





# Serializers.serializers 

# def name_lenght(value):   # Validator 
#     if len(value)< 2:
#         raise serializers.ValidationError("Name length is too short")

# class movieserializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=100,validators = [name_lenght])
#     description = serializers.CharField(max_length=200)
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return movie.objects.create(**validated_data)
    
#     def update(self,instance, validated_data): # instance carries the old data and validated_data is the new data
        
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance
#     def validate_name(self,value):  # field level validation 
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         return value
    
#     def validate(self,value): # object level validation
#         if value['name'] == value['description']:
#             raise serializers.ValidationError("Name and description should be different")
#         else : 
#             return value
        