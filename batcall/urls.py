from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_panel'),
    path('', views.homepage, name="home"),
    path('blog/', include('blog.urls'), name="blog_page"),
    path('forms/', include('forms.urls'), name="forms_page"),
    path('importants/', include('importants.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)