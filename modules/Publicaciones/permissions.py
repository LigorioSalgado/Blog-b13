from rest_framework import permissions

class GroupPermission(permissions.BasePermission):
    message = "Usted no es parte de este grupo"
    SELECTED_GRUPO = "Writers"
    def has_permission(self, request, view):

        if request.user.groups.filter(name=self.SELECTED_GRUPO) and request.method == 'GET':
            return True
        else:
            return False


class OnlyGetPermission(permissions.BasePermission):

    def has_permission(self,request,view):

        if request.user is None and request.method == "GET":
            return True
        else:
            return False
