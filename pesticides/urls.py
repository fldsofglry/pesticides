from django.urls import path

from . import views

app_name = "pesticides"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:record_id>/", views.detail, name="detail"),
    path("delete_record/<int:record_id>/", views.delete_record, name="delete_record"),
]
