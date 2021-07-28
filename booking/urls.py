from django.urls import include, path

from . import views

app_name='booking'

urlpatterns = [
   
    path('',views.findbus,name='findbus'),
    path('bookings/',views.booking_list,name='booking_list'),
    path('seebookings/',views.seebookings,name='seebookings'),
    path('cancelling/',views.cancelling,name='cancelling'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout')
]
