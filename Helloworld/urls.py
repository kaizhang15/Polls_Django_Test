from django.conf.urls import url, include
from django.contrib import admin

from . import view
from . import mainpage

urlpatterns = [
    url(r'^$', mainpage.main_page),
    url(r'^hello$', view.hello),
    url(r'^html_test$', view.html_test),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
#    url(r'^templates/images/(?P<path>.*)', 'django.views.static.serve', {'document_root':'/home/ubuntu/django_test/Helloworld/templates/images'}),

]



