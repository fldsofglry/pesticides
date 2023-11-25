from django.urls import path

from . import views

app_name = "pesticides"
print('hit here in urls.py')
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:record_id>/", views.detail, name="detail"),
    path("delete_record/<int:record_id>/", views.delete_record, name="delete_record"),
    path("add_record/", views.add_record, name="add_record"),
]
