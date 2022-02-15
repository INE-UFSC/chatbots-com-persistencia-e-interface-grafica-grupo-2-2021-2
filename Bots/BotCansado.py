from Bots.Bot import Bot
from Bots.Comando import Comando
from Database.BotDAO import DAO


class BotCansado(Bot):
    def __init__(self, nome):
        self.__nome = nome
        self.__json_path = "Database/BotCansado"
        self.__dao = DAO(self.__json_path)
        self.__comandos = []

        comandos_dao = self.__dao.get_all()

        try:
            for key, value in comandos_dao.items():
                self.__comandos.append(Comando(key, value[0], value[1]))
        except Exception as e:
            print(e)

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def apresentacao(self):
        return "Cara, escolhe outro maluco aí pq num quero papo não"

    def mostra_comandos(self):
        mensagem = ""
        for comando in self.__comandos:
            mensagem += f"{comando.id} - {comando.mensagem} \n"
        return mensagem

    def executa_comando(self, cmd):
        for comando in self.__comandos:
            if comando.id == cmd:
                return comando.getRandomResposta()

        return 'Comando não encontrado'

    def boas_vindas(self):
        return "Seja bem-vindo(a)."

    def despedida(self):
        return "Foi um prazer. Volte sempre."
