from rest_framework import permissions
from adminapp.models import Admin
from rest_framework import exceptions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = request.user.id
        admin = Admin.objects.filter(id=user_id).first()
        if admin:
            return True
        else:
            raise exceptions.PermissionDenied(
           {'error':'You do not have permission to perform this action.',
            'message':'Only admin can access this route.'})
            