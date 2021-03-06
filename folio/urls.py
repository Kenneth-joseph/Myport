from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/project$', views.new_project, name='new_project'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/profile/update$', views.update_profile, name='update_profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
