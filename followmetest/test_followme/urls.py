from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("reg", views.insertView, name="reg"),
    path("insertdata", views.insert_data, name="insertdata"),
    path("showdata", views.showData, name="showData"),
    path("editdata/<int:pk>", views.editData, name="editData"),
    path("updatedata/<int:pk>", views.updateData, name="updateData"),
    path("deletedata/<int:pk>", views.deleteData, name="deleteData"),
    path("register/", views.newreg, name="newreg"),
    path("registered/", views.register, name="registered"),
    path("login/", views.loginPage, name="loginPage"),
    path("loginuser/", views.loginUser, name="loginUser"),
    path("logout/", views.logout, name="logout")
]