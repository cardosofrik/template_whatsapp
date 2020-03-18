from django.urls import path
from enviar_msg.views import MensagemWhatsAppView
urlpatterns = [


    path('', MensagemWhatsAppView.as_view(), name='_enviar')
]
