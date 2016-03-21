from tastypie.resources import ModelResource

from .models import Book, Profile

class BookResource(ModelResource):

    class Meta:
        queryset = Book.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        always_return_data = True
        resource_name = 'books'


class ProfileResource(ModelResource):

    class Meta:
        queryset = Profile.objects.all()
        resource_name = 'profile'