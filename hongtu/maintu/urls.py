from django.conf.urls import url

from . import views


urlpatterns = [
   url(r'^$', views.index, name='index'),
	url(r'^index1$', views.index1, name='index1'),
	# ex: /polls/5/
    url('^detail/(\d+)', views.detail, name='detail'),
 url('^detail1/(\d+)', views.detail1, name='detail1'),
    # ex: /polls/5/results/
    url('(\d+)/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    url('<int:question_id>/vote/', views.vote, name='vote'),
]
