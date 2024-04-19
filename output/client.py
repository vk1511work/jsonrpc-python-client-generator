from jsonrpc_python_client_generator.client import HttpClient
from jsonrpc_python_client_generator.response import Success, Error
from typing import Union

class JsonRpcClient:

    client: HttpClient

    def __init__(self) -> None:
        self.client = HttpClient(url='https://api.sweb.ru/notAthorized')

    def getToken(self,login: str, password: str = None) -> Union[Success,Error]:
        '''Получение нового токена для авторизации

        Keyword arguments:
        login -- Логин
        password -- Пароль
        '''
        return self.client.post(method='getToken',params={"login":login,"password":password})

    def checkLogin(self,login: str) -> Union[Success,Error]:
        '''Проверка доступности логина для регистрации

        Keyword arguments:
        login -- Желаемый логин пользователя
        '''
        return self.client.post(method='checkLogin',params={"login":login})
    

client = JsonRpcClient()
print(client.checkLogin(login="dddsf"))