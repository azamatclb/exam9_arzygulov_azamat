from django.urls import path

from webapp.views.albums import AlbumDetailView, AlbumCreateView, AlbumUpdateView, AlbumDeleteView
from webapp.views.pictures import PictureListView, PictureAddView, PictureDeleteView, PictureUpdateView, \
    PictureDetailView

app_name = 'webapp'

urlpatterns = [
    path('', PictureListView.as_view(), name='pictures'),
    path('picture/add/', PictureAddView.as_view(), name='picture_add'),
    path('picture/<int:pk>/delete/', PictureDeleteView.as_view(), name='picture_delete'),
    path('picture/<int:pk>/update/', PictureUpdateView.as_view(), name='picture_update'),
    path('picture/<int:pk>/detail/', PictureDetailView.as_view(), name='picture_detail'),
    path('album/<int:pk>/detail/', AlbumDetailView.as_view(), name='album_detail'),
    path('album/add/', AlbumCreateView.as_view(), name='album_create'),
    path('album/<int:pk>/edit/', AlbumUpdateView.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', AlbumDeleteView.as_view(), name='album_delete'),
]
