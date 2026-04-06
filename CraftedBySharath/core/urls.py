from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("api/services/click/", views.service_click, name="service_click"),
    path("api/rag/chat/", views.rag_chat, name="rag_chat"),
]