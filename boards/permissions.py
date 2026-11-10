from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование объекта только его владельцу (owner).
    Остальные могут только читать (GET, HEAD, OPTIONS).
    """
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено любым запросом (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Запись разрешена только владельцу проекта/объекта
        return obj.owner == request.user
