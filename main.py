"""Исследования на тему SIP TLS соединение - точка входа"""
import ssl
import socket

# Детали SIP сервера
SIP_SERVER_HOST = 'sip.example.com'  # Адрес SIP сервера
SIP_SERVER_PORT = 5061  # Порт SIP сервера

# Создаем сокет и оборачиваем его в SSL контекст
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем TCP сокет
ssl_context = ssl.create_default_context()  # Создаем SSL контекст по умолчанию
ssl_socket = ssl_context.wrap_socket(s, server_hostname=SIP_SERVER_HOST)  # Оборачиваем сокет в SSL контекст

# Подключаемся к SIP серверу
ssl_socket.connect((SIP_SERVER_HOST, SIP_SERVER_PORT))

# Отправляем SIP сообщение
message = 'REGISTER sip:{} SIP/2.0\r\n\r\n'.format(SIP_SERVER_HOST)  # Создаем SIP сообщение
ssl_socket.send(message.encode())  # Отправляем SIP сообщение на сервер

# Получаем ответ от SIP сервера
response = ssl_socket.recv(4096)
print(response.decode())

# Закрываем SSL сокет
ssl_socket.close()



def main():
    pass


if __name__ == '__main__':
    main()
