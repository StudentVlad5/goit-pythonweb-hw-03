import json
import urllib.parse
from datetime import datetime
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader

# Налаштування Jinja2 для поточної директорії
env = Environment(loader=FileSystemLoader('.'))

class MyFramework(BaseHTTPRequestHandler):
    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        path = pr_url.path

        # Маршрутизація сторінок
        if path == '/':
            self.send_static_file('index.html', 'text/html')
        elif path == '/message':
            self.send_static_file('message.html', 'text/html')
        elif path == '/read':
            self.render_read_page()
        # Обробка конкретних статичних файлів у корені
        elif path == '/style.css':
            self.send_static_file('style.css', 'text/css')
        elif path == '/logo.png':
            self.send_static_file('logo.png', 'image/png')
        else:
            self.send_static_file('error.html', 'text/html', 404)

    def do_POST(self):
        if self.path == '/message':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            parsed_data = urllib.parse.parse_qs(post_data.decode('utf-8'))
            username = parsed_data.get('username', [''])[0]
            message = parsed_data.get('message', [''])[0]

            self.save_to_json(username, message)

            # Редирект
            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()

    def send_static_file(self, filename, content_type, status=200):
        file_path = Path(filename)
        if file_path.exists():
            self.send_response(status)
            self.send_header('Content-type', content_type)
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            # Якщо файл не знайдено фізично, хоча маршрут правильний
            if filename != 'error.html':
                self.send_static_file('error.html', 'text/html', 404)

    def render_read_page(self):
        data_file = Path('storage/data.json')
        messages = {}
        if data_file.exists():
            with open(data_file, 'r', encoding='utf-8') as f:
                try:
                    messages = json.load(f)
                except json.JSONDecodeError:
                    messages = {}
        
        template = env.get_template('read.html')
        content = template.render(messages=messages)
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))

    def save_to_json(self, username, message):
        storage_dir = Path('storage')
        storage_dir.mkdir(exist_ok=True) 
        file_path = storage_dir / 'data.json'
        
        data = {}
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    pass

        data[str(datetime.now())] = {"username": username, "message": message}

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def run():
    server_address = ('', 3000)
    http = HTTPServer(server_address, MyFramework)
    print("Сервер запущено на порту 3000...")
    http.serve_forever()

if __name__ == '__main__':
    run()