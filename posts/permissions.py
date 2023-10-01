from rest_framework.permissions import BasePermission,SAFE_METHODS
#SAFE_METHODS means the methods which will not allow for the creation or moodificaion of data only reading (GET, HEAD, OPTIONS),

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
    
class AuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author