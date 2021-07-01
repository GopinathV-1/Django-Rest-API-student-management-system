from rest_framework import viewsets
from .serializers import AssignmentSerializer
from .models import Assignment
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.authentication import (TokenAuthentication,
                                           BasicAuthentication)


class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    authentication_classes = [BasicAuthentication, TokenAuthentication]

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            self.permission_classes = [permissions.IsAdminUser, ]
        elif self.action in ['list']:
            self.permission_classes = [permissions.IsAuthenticated, ]
        else:
            pass
        return super(self.__class__, self).get_permissions()

    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('due_date').first()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
