from rest_framework import generics,permissions
from .models import Posts
from .serializers import PostSerializer
from rest_framework import permissions #authorization
from blog.permissions import IsOwner


class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner)

    def perform_create(self, serializer):
        """associating the user that created the post, with the post instance.
        we override the perform create method 

        Args:
            serializer ([type]): [description]
        """
        serializer.save(owner=self.request.user)   

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,IsOwner) #denies permissions to 
    #unauthenticated users
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly) => can be used for unauthenticated users 
    #hence risky than the first isauthenticated permission

