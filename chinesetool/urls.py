from django.conf.urls import include, patterns, url

from chinesetool import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^translate_word/$', views.translate_word, name='translate_word'),
    url(r'^translate_sentence/$', views.translate_sentence, name='translate_sentence'),
    url(r'login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^register/$', views.register_page, name='register'),
    url(r'^dictionary/$', views.dictionary, name='dictionary'),
    url(r'^choose_language/$', views.choose_language, name='choose_language'),
    url(r'^add_lesson/$', views.add_lesson, name='add_lesson'),
    url(r'^modify_lesson/(\d+)/$', views.modify_lesson, name='modify_lesson'),
    url(r'^add_requirement/(\d+)/$', views.add_requirement, name='add_requirement'),
    url(r'^i18n/', include('django.conf.urls.i18n')),

)