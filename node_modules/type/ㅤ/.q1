import subprocess
import time
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from datetime import datetime

console = Console()

class SimplePHPServer:
    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = port
        self.process = None

    def start_server(self):
        directory = os.getcwd()
        try:
            self.process = subprocess.Popen(
                ["php", "-S", f"{self.host}:{self.port}", "-t", directory],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=1,
                universal_newlines=True
            )
            time.sleep(1)
            return self.process
        except FileNotFoundError:
            console.print(Panel("PHP is not installed or not in PATH", style="bold red"))
            return None

    def parse_log_line(self, line: str):
        if "GET" in line or "POST" in line:
            parts = line.split()
            if len(parts) >= 3:
                ip = parts[1].split(":")[0]
                return ip
        return None

    def monitor_logs(self):
        while self.process and self.process.poll() is None:
            output = self.process.stdout.readline()
            if output:
                ip = self.parse_log_line(output)
                if ip:
                    console.clear()
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    text = Text.assemble(
                        ("Visitor IP: ", "bold yellow"),
                        (ip, "bold cyan"),
                        (" | Access Time: ", "bold yellow"),
                        (timestamp, "bold green")
                    )
                    panel = Panel(text, title="New Visitor", title_align="center", border_style="bright_blue")
                    console.print(panel)
                    time.sleep(1)

    def stop_server(self):
        if self.process:
            self.process.terminate()
            print()
            console.print(Panel("Server stopped", style="bold yellow", border_style="red"))

def main():
    console.clear()
    php_server = SimplePHPServer()
    console.print(Panel("© Wanz Xploit", style="bold green", border_style="blue"))
    console.print(Panel("Starting MATA Server...", style="bold green", border_style="green"))
    process = php_server.start_server()

    if process is None:
        console.print(Panel("Error: Unable to start server.", style="bold red"))
        return

    url = f"http://{php_server.host}:{php_server.port}"
    console.print(Panel(f"MATA Server running at [bold blue]{url}[/]", style="bold green", border_style="blue"))

    try:
        php_server.monitor_logs()
    except KeyboardInterrupt:
        php_server.stop_server()
    except Exception as e:
        php_server.stop_server()
        console.print(Panel(f"Error: {str(e)}", style="bold red"))

if __name__ == "__main__":
    main()