from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Book, Profile

class BookResource(ModelResource):

    class Meta:
        queryset = Book.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        resource_name = 'books'
        authorization = Authorization()


class ProfileResource(ModelResource):

    class Meta:
        queryset = Profile.objects.all()
        allowed_methods = ['get', 'post', 'put']
        resource_name = 'profile'