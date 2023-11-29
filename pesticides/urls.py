from django.urls import path

from . import views

app_name = "pesticides"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:record_id>/", views.detail, name="detail"),
    path("delete_record/<int:record_id>/", views.delete_record, name="delete_record"),
    path("update_record/<int:record_id>/", views.update_record, name="update_record"),
    path("add_record/", views.add_record, name="add_record"),
    path("formula/", views.FormulaView.as_view(), name="formula"),
    path("formula/<int:pk>/", views.FormulaDetailView.as_view(), name="formula_detail"),
    path("formula/add_formula/", views.add_formula, name="add_formula"),
]
