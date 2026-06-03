from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
  # The QuerySet is keeping track of all the visits to the Home Page.
  queryset = PageVisit.objects.all()
  page_qs = queryset.filter(path=request.path)
  PageVisit.objects.create(path= request.path)

  path = request.path
  print(f"Visited {path}")
  return render(request, "home.html", {"visits": page_qs.count(), "total_visits": queryset.count()})