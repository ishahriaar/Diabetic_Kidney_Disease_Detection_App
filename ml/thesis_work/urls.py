from django.urls import path
from .views import ed_user_input_view, home_page_view, dkd_user_input_view


urlpatterns = [
    path('', home_page_view, name='home'),
    path('ed/', ed_user_input_view, name='ed'),
    path('dkd/', dkd_user_input_view, name='dkd'),
]
