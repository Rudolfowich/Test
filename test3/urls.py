from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', ArticleListView.as_view(), name='home'),
                  path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
                  path('create_article', ArticleCreateView.as_view(), name='create_article'),
                  path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
                  path('login', UserLoginView.as_view(), name='login'),
                  path('register', RegisterUserView.as_view(), name='register'),
                  path('logout', LogoutUserView.as_view(), name='logout'),
                  path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
