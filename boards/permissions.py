import importlib

try:
    permissions = importlib.import_module("rest_framework").permissions
except ModuleNotFoundError:
    class _FallbackPermissions:
        SAFE_METHODS = ("GET", "HEAD", "OPTIONS")

        class BasePermission:
            def has_permission(self, request, view):
                return True

            def has_object_permission(self, request, view, obj):
                return True

    permissions = _FallbackPermissions()


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
        return getattr(obj, "owner", None) == request.user
