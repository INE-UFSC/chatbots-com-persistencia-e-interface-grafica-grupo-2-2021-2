from random import randint


class Comando:
    def __init__(self, id: int, msg: str, respostas=[]):
        self.__id = id
        self.__msg = msg
        self.__respostas: list = respostas

    @property
    def id(self):
        return self.__id

    @property
    def mensagem(self):
        return self.__msg

    def getRandomResposta(self):
        if len(self.__respostas) == 0:
            return None
        index = randint(0, len(self.__respostas) - 1)
        return self.__respostas[index]

    def addResposta(self, resposta):
        if type(resposta) == str and resposta not in self.__respostas:
            self.__respostas.append(resposta)

    def delResposta(self, resposta):
        try:
            self.__respostas.remove(resposta)
        except ValueError:
            print('Resposta não existe')
        except Exception as e:
            print(f"Unknown Error: {e}")
