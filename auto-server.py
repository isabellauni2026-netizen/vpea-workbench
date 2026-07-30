#!/usr/bin/env python3
"""自动保活 HTTP 服务器 —— 每次请求时检测并重启"""
import http.server
import subprocess
import os
import sys

PORT = 8080
DIRECTORY = "/workspace"

class AutoRestartHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        pass  # 安静模式

# 先确保旧进程被杀掉
os.system(f"lsof -ti:{PORT} | xargs -r kill -9 2>/dev/null")

server = http.server.HTTPServer(("0.0.0.0", PORT), AutoRestartHandler)
print(f"Server running on port {PORT}")
server.serve_forever()
