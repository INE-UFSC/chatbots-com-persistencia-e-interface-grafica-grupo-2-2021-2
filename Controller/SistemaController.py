from Bots.Bot import Bot
from View.TelaInicial import ClienteView


class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        self.__view = ClienteView()
        self.__bot = None
        self.__lista_bots = []
        try:
            for bot in lista_bots:
                if isinstance(bot, Bot):
                    self.__lista_bots.append(bot)
        except Exception as e:
            print(e)

    def mostra_menu(self):
        self.__view.tela_escolha(self.__lista_bots)

    def mostra_chat(self, bot: Bot):
        self.__view.tela_conversa_bot(self, bot.boas_vindas())
        client_message = self.__view.get_message()
        response = bot.executa_comando(client_message)
        self.__view.escreve(response)

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())

    def inicio(self):
        self.mostra_menu()
        eventos = self.__view.le_eventos()

        while True:
            self.mostra_comandos_bot()
            fechar_programa = self.le_envia_comando()

            if fechar_programa:
                self.__bot.despedida()
                break
            print()
