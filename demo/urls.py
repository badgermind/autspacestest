from django.urls import path
from .views import AboutPageView, AutismPageView, HomePageView, \
     ModeratePageView, MyStoriesPageView, ShareStoriesPageView, \
     ViewStoriesPageView, OverviewPageView, RegistrationPageView, \
     LogoutPageView

app_name = 'demo'

urlpatterns = [
    path("about", AboutPageView.as_view(), name="about"),
    path("autism", AutismPageView.as_view(), name="autism"),
    path("", HomePageView.as_view(), name="home"),
    path("moderate", ModeratePageView.as_view(), name="moderate"),
    path("mystories", MyStoriesPageView.as_view(), name="mystories"),
    path("sharestories", ShareStoriesPageView.as_view(), name="sharestories"),
    path("viewstories", ViewStoriesPageView.as_view(), name="viewstories"),
    path("overview", OverviewPageView.as_view(), name="overview"),
    path("registration", RegistrationPageView.as_view(), name="registration"),
    path("logout", LogoutPageView.as_view(), name="logout"),
]