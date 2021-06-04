from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from TriviaApp import views

urlpatterns = [
    url(r'^bibleQuestion/$', views.bibleQuestionApi),
    url(r'^bibleQuestion/([0-9]+)$', views.bibleQuestionApi),

    url(r'^questionInfo/$', views.questioInfoApi),
    url(r'^questionInfo/([0-9]+)$', views.questioInfoApi),

    url(r'^saveFile$', views.saveFile)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
