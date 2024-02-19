from django.contrib import admin
from django.urls import path, include
from notes.views import login_view, signup_view, success_url
from notes.views import create_note, NoteDetailView, share_note, update_note, NoteVersionHistoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('success_url/', success_url, name='success_url'),

    path('notes/create/', create_note),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/share/', share_note),
    path('notes/<int:pk>/update/', update_note),
    path('notes/version-history/<int:pk>/', NoteVersionHistoryView.as_view(), name='note-version-history'),
]
