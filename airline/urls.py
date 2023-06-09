from django.urls import path
from . import views

app_name = "airline"
urlpatterns = [
    path("", views.main, name="main"),
    path("staff/", views.staff, name="staff"),
    path("passager/<int:passager_id>", views.passager, name="passager"),
    path("flight/<int:fli_id>", views.flight, name="flight"),
    path("airport/<int:airport_id>", views.airport, name="airport"),
    path("add_data/", views.add_data, name="add_data"),
    path("routes/<int:route_id>", views.routes, name="routes"),
    path("country/", views.country, name="country"),
    path("all", views.all, name="all"),
    path("create_message", views.create_message, name="create_message"),
    path("new_message/<int:user_id>", views.new_message, name="new_message"),
]
