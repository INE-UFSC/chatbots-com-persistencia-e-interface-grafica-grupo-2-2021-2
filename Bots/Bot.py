from abc import ABC, abstractmethod


class Bot(ABC):
    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = {"1": "Boas vindas",
                           "2": "Despedida"}

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def mostra_comandos(self) -> str:
        comandos = '# Comandos \n'
        for cmd, value in self.comandos.items():
            comandos += f'[{cmd}]: {value} \n'
        return comandos

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass

    @abstractmethod
    def despedida():
        pass


if __name__ == "__main__":
    botTeste = Bot('Jose')
    print(botTeste.mostra_comandos())
