import PySimpleGUI as sg


class ClienteView():
    def __init__(self):
        self.__container = []
        self.__window = sg.Window("1Choose one Bot to talk: ", self.__container,
                                  font=("Helvetica", 14))

    def tela_escolha(self, bots):
        sg.theme('black')
        for index, bot in enumerate(bots, start=1):
            item = [sg.Text(f'{index} - Bot: {bot.nome} -- {bot.apresentacao()}')]
            self.__container.append(item)

        item = [sg.Text('Bot Number: '), sg.InputText('', key='botNumber')]
        self.__container.append(item)

        self.__window = sg.Window("Choose one Bot to talk: ", self.__container,
                                  font=("Helvetica", 14))

    def __validate_int_input(self, user_input) -> bool:
        pass

    def le_eventos(self):
        return self.__window.read()

    def limpa_caixa(self, key):
        return self.__window.Element(key).Update('')

    def fim(self):
        self.__window.close()
