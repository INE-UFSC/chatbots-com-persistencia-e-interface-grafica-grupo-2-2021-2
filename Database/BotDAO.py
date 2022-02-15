import json


class DAO:
    def __init__(self, path: str) -> None:
        self.__connected = False
        self.__path = path
        self.__cache = {}

        try:
            self.__load()
            self.__connected = True
            print(f'Arquivo {path}.json aberto com sucesso')
        except:
            print('Erro na hora de abrir o arquivo, tente outro nome')

    @property
    def connected(self) -> bool:
        return self.__connected

    def __dump(self) -> None:
        if self.__connected:
            try:
                with open(f'{self.__path}.json', 'w') as file:
                    json.dump(self.__cache, file)
            except Exception as e:
                print(e)

    def __load(self):
        with open(f'{self.__path}.json', 'r') as file:
            self.__cache = json.load(file)

    def get_all(self) -> dict:
        self.__load()
        return self.__cache
