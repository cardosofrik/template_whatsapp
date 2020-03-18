from django import forms


class MensagemWhatsAppForm(forms.Form):

    mensagem = forms.CharField()
