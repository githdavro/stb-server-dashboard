import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class UnifiedArmbianServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ['/api/status', '/api/status/']:
            try:
                # STORAGE
                stat = os.statvfs('/')
                total_storage = stat.f_blocks * stat.f_frsize
                free_storage = stat.f_bavail * stat.f_frsize
                used_storage = total_storage - free_storage
                storage_percentage = round((used_storage / total_storage) * 100, 1)
                storage_total_gb = round(total_storage / (1024 ** 3), 2)
                storage_used_gb = round(used_storage / (1024 ** 3), 2)
                storage_available_gb = round(free_storage / (1024 ** 3), 2)

                # RAM
                meminfo = {}
                with open('/proc/meminfo', 'r') as f:
                    for line in f:
                        parts = line.split(':')
                        key = parts[0]
                        value = int(parts[1].strip().split()[0])
                        meminfo[key] = value

                total_ram_kb = meminfo.get('MemTotal', 0)
                available_ram_kb = meminfo.get('MemAvailable', 0)
                used_ram_kb = total_ram_kb - available_ram_kb
                ram_percentage = round((used_ram_kb / total_ram_kb) * 100, 1)
                ram_total_gb = round(total_ram_kb / 1024 / 1024, 2)
                ram_used_gb = round(used_ram_kb / 1024 / 1024, 2)

                # TEMPERATURE
                temperature = 0.0
                thermal_path = '/sys/class/thermal/thermal_zone0/temp'
                if os.path.exists(thermal_path):
                    with open(thermal_path, 'r') as f:
                        temperature = round(int(f.read()) / 1000, 1)

                # UPTIME
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.read().split()[0])
                days = int(uptime_seconds // 86400)
                hours = int((uptime_seconds % 86400) // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                uptime = f"{days}d {hours}h {minutes}m"

                # CPU LOAD
                load1, _, _ = os.getloadavg()
                cpu_count = os.cpu_count() or 1
                cpu_usage = round((load1 / cpu_count) * 100, 1)
                if cpu_usage < 0:
                    cpu_usage = 0
                if cpu_usage > 100:
                    cpu_usage = 100

                # CPU INFO
                cpu_freq_mhz = 0
                cpu_freq_ghz = 0
                cores = os.cpu_count() or 1
                cpuinfo_path = '/proc/cpuinfo'
                if os.path.exists(cpuinfo_path):
                    with open(cpuinfo_path, 'r') as f:
                        lines = f.readlines()
                    freqs = []
                    for line in lines:
                        if 'cpu MHz' in line:
                            mhz = float(line.split(':')[1].strip())
                            freqs.append(mhz)
                    if freqs:
                        cpu_freq_mhz = round(sum(freqs) / len(freqs), 0)
                        cpu_freq_ghz = round(cpu_freq_mhz / 1000, 2)

                # JSON RESPONSE
                data = {
                    "cpu_usage": cpu_usage,
                    "cpu_cores": cores,
                    "cpu_freq_mhz": cpu_freq_mhz,
                    "cpu_freq_ghz": cpu_freq_ghz,
                    "ram_percentage": ram_percentage,
                    "ram_used": ram_used_gb,
                    "ram_total": ram_total_gb,
                    "storage_percentage": storage_percentage,
                    "storage_used": storage_used_gb,
                    "storage_available": storage_available_gb,
                    "storage_total": storage_total_gb,
                    "temperature": temperature,
                    "uptime": uptime
                }

                payload = json.dumps(data).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(payload)

            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(e).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 5000
    print(f'Armbian API running at http://{HOST}:{PORT}')
    server = HTTPServer((HOST, PORT), UnifiedArmbianServer)
    server.serve_forever()
