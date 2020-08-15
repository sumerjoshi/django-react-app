from leads.models import Leads
from rest_framework import viewsets, permissions
from leads.serializers import LeadSerializer

# Lead Viewset
'''
Allows to create a CRUD API without having to explain
specfic functions. Very similar to Ruby on Rails.

Look at viewsets on the Django Application Doc.

https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

'''


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = LeadSerializer
