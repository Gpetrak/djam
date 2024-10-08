import logging

from rest_framework import viewsets, views, permissions
from rest_framework.response import Response

from apps.privilege_manager.models import Team
from apps.privilege_manager.serializers import GroupSerializer

logger = logging.getLogger(__name__)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = GroupSerializer


class GeoServerRolesView(views.APIView):
    """
    Endpoint returning User permission groups, which in terminology of Geoserver are called 'roles'
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        groups_pbjects = Team.objects.all()
        group_names = [group.name for group in groups_pbjects]

        return Response({"groups": group_names})


class GeoServerAdminRoleView(views.APIView):
    """
    Endpoint returning name of admin User permission group, which in terminology of Geoserver is called 'adminRole'
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response({"adminRole": "admin"})
