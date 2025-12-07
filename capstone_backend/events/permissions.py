from rest_framework import permissions

class IsSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['seller', 'both']


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.seller == request.user
