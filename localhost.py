import socket
import subprocess
import webbrowser

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

PORTS = [8082, 8083, 8084, 8085]
selected_port = None

for port in PORTS:
    if not is_port_in_use(port):
        selected_port = port
        break

if selected_port is None:
    print("Varsayılan portlardan hiçbiri (8082-8085) kullanılabilir değil.")
    while True:
        try:
            user_port = int(input("Lütfen kullanılabilir bir port belirtin: "))
            if is_port_in_use(user_port):
                print(f"Port {user_port} kullanımda. Lütfen başka bir port seçin.")
            else:
                selected_port = user_port
                break
        except ValueError:
            print("Geçersiz giriş. Lütfen sayısal bir port numarası girin.")
else:
    print(f"Port {selected_port} kullanılabilir.")

print(f"HTTP sunucusu {selected_port} portunda başlatılıyor...")
subprocess.Popen(["python", "-m", "http.server", str(selected_port)])

# Varsayılan tarayıcıyı seçilen port ile açma
webbrowser.open(f"http://localhost:{selected_port}")
