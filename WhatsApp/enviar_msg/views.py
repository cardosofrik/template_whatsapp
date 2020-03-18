from django.shortcuts import render
from enviar_msg.forms import MensagemWhatsAppForm

from django.views.generic.base import View


class MensagemWhatsAppView(View):
    PAGINA_WHTS = "index.html"

    def get(self, request):
        return render(request, self.PAGINA_WHTS)

    def post(self, request):
        self.mensagem_enviada = ''
        self.numero =''
        self.mensagem_escrita =''


        formulario = MensagemWhatsAppForm(request.POST)

        if formulario.is_valid():
            mensagem_preparada = formulario.data
            self.mensagem_escrita = mensagem_preparada['mensagem']

            if self.mensagem_escrita in ' ':
                self.mensagem_enviada = "nao enviado, Campo em branco!"

            else:
                self.mensagem_enviada = "enviada"
                for lista_numeros in self.numero:
                    numero_dos_grupos = lista_numeros.grupos_encontrados

                    
        conteudo = dict()
        conteudo['numeros'] = self.numero
        conteudo['aviso'] = self.mensagem_enviada
        conteudo['mensagem_esc'] = self.mensagem_escrita

        return render(request, self.PAGINA_WHTS, conteudo)

