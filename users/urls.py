

from django.urls import path
from .views import UserView, GroupView, SingleGroupView, MyUserDataView, SingleUserView

from .views import SignUpView



#from rest_framework_jwt.views import obtain_jwt_token



###

from knox import views as knox_views
from users.views import LoginView

###

app_name = "users"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>', SingleUserView.as_view()),


    path('my_user_data/', MyUserDataView.as_view()),

    path('groups/', GroupView.as_view()),
    path('groups/<int:pk>', SingleGroupView.as_view()),
    path('signup/', SignUpView.as_view(), name='signup'),


    path('api/token-auth/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),

    #path('api-token-auth/', obtain_jwt_token),


]
