"""BikenPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import django
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
#from django.contrib.auth.views import login,logout_then_login
from principal.views import index, home,registro,login,endReg, quienesSomos,contacto,murouser,uploadBike,endUploadBike

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls), 
    path('',index,name ='index'),
    path('home/',home,name ='home'),
    path('registro/',registro, name='registro'),
    path('login/',login, name='login'),
    path('uploadBike/' , uploadBike, name='uploadbike'),
    path('murouser/' , murouser, name='murouser'),
    path('endReg/' , endReg, name='messagereg'),
    path('endUploadBike/' , endUploadBike, name='messagebike'),
    path('quienessomos/' , quienesSomos, name='quienessomos'),
    path('contacto/' , contacto, name='contacto'),
    path('accounts/',include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)