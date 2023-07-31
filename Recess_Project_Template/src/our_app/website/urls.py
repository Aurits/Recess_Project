from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('course', views.course, name='course'),
    path('facility', views.facility, name='facility'),
    path('instructor', views.instructor, name='instructor'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('courses', views.courses, name='courses'),
    path('facilities', views.facilities, name='facilities'),
    path('instructors', views.instructors, name='instructors'),
    path('signout', views.signout, name='sign_out'),
    path('signin', views.signin, name='sign_in'),
    path('signup', views.signup, name='sign_up'),
    path('profile', views.profile, name='profile'),
]
