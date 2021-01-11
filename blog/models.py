from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length= 20)
    #creating authentication using django's User model
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, default= 1)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return"{}".format(self.title)

    class Meta:
        verbose_name_plural = 'Posts'  
    
