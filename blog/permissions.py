from rest_framework.permissions import BasePermission
from .models import Posts


class IsOwner(BasePermission):
    """Custom permission class to allow only posts owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the posts owner."""
        if isinstance(obj, Posts):
            return obj.owner == request.user
        return obj.owner == request.user