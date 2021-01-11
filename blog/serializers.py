from rest_framework import serializers
from .models import Posts


#For the most part, any changes you make 
#in your model should be reflected in your 
#serializers too. This is because serializers 
#interface directly with the model 
#which aids in changing weird-looking 
#query sets to json and vice versa.


class PostSerializer(serializers.ModelSerializer):
    """Posts serializer to map the model instance into json format

    Args:
        serializers ([type]): [description]
    """
    class Meta:
        model = Posts
        #read only means that a user cannot alter the owner of a post
        owner = serializers.ReadOnlyField(source='owner.username')
        fields =('title','id','body','owner','created_at') #fields = '__all__'
        #exclude = [''] => list of fields to be excluded/not serialized