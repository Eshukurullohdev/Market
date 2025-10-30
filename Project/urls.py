from django.urls import path
from .views import  *

urlpatterns = [
     path('', home, name='home'),
     path("topshirish/", topshirish, name='topshirish'),
     path("sotuvchi/", Sotuvchi, name='sotuvchi'),
     path("sotuvchi_bolish/", sotuvchi_bolish, name='sotuvchi_bolish'),
     path("savat/", savat, name='savat'),
     path("savol/", savol_javob, name="savol"),
     path("qoshimcha/", qoshimcha_tovar, name="qoshimcha_tovar"),
     path("register/", register, name="register"),
     path("login/", login, name="login"),
     path("detail/<int:pk>/", Detail_Tovar, name="detail_tovar"),
     path("logout/", logout, name="logout"),
     path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
     path("oddiy/", purchase, name="purchase"),
];



