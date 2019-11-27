from django.urls import path
from rooms import views as room_views

app_name = "core"

# url은 함수만 갖고 올 수 있습니다. HomeView는 class이므로, as_view()를 사용합니다.
urlpatterns = [path("", room_views.HomeView.as_view(), name="home")]
