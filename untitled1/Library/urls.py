from django.conf.urls import url
from django.conf.urls.static import static
from . import views
urlpatterns = [
    #/Library/
    url(r'^$', views.index, name='index'),
    url(r'^welcome/$', views.welcome, name='welcome'),
    url(r'^home/$',views.home,name='home'),

    #/Library/id
    url(r'^(?P<isbn>[0-9]+)/$', views.detail, name='detail'),
    url(r'^signup/$', views.signup, name='signup'),

    url(r'^login/$', views.login_user, name='login1'),
    url(r'^search/$', views.search, name='search'),
    url(r'^logout/$',views.logout_user,name = 'logout'),
    url(r'^(?P<isbn>[0-9]+)/borrow/$', views.borrow, name='borrow'),
    url(r'^borrow/books/$',views.book_borrowed,name='book_borrow'),
    url(r'^books/$',views.borrowed_books,name = 'borrowed_books'),
    url(r'^admin/borrow$',views.issue_books,name='issue_books'),
    url(r'^(?P<isbn>[0-9]+)/add_feedback/$',views.create_feedback, name = "add_feedback"),
    url(r'^admin/accept/(?P<isbn>[0-9]+)/$',views.book_accept,name= 'book_accept'),
    url(r'^admin/reject/(?P<isbn>[0-9]+)/$',views.book_reject,name= 'book_reject'),
    url(r'^(?P<isbn>[0-9]+)/return/$',views.book_return , name = "book_return"),
    url(r'^all_books$',views.books_all,name = 'books'),
    url(r'^feedback/(?P<isbn>[0-9]+)$',views.add_feedback,name='feedback'),
    url(r'^download/(?P<fine>[0-9]+)$',views.download,name='download'),
    url(r'^fine',views.fine,name='fine'),
]