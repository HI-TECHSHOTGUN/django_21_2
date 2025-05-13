from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети
html_file_path = "page_4.html"  # Путь к HTML-файлу (относительно текущей директории)


class MyServer(BaseHTTPRequestHandler):
    """
        Специальный класс, который отвечает за
        обработку входящих запросов от клиентов
    """

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        try:
            with open(html_file_path, "r", encoding="utf-8") as f:  # Открываем HTML файл
                html_content = f.read()

            self.send_response(200)  # Отправка кода ответа
            self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
            self.end_headers()  # Завершение формирования заголовков ответа
            self.wfile.write(bytes(html_content, "utf-8"))  # Тело ответа

        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("File not found.", "utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Cтарт веб-сервера
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Корректная остановка веб-сервера
    webServer.server_close()
    print("Server stopped.")
