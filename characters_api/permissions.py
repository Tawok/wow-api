from rest_framework import permissions


class IsStaffPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        """Checks if the authenticated user has permissions"""
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

    """ def has_object_permission(self, request, obj):
        #Check if the logged in user has permission to perform this action
        if request.user == obj.user :
            return True
        return False """
