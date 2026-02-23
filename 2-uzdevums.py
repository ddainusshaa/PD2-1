nodes = [
    "Srv-Web-01;192.168.1.10;15;UP",
    "Srv-DB-01;192.168.1.20;450;UP",
    "Srv-Backup;10.0.0.5;0;DOWN",
    "Workstation-A;192.168.1.105;5;UP",
    "Srv-Proxy-01;172.16.0.1;10;up",
    "Srv-Mail;10.0.0.10;120;UP",
    "Router-Core;192.168.1.1;2;UP",
    "Srv-Dev-01;192.168.2.50;500;UP",
    "Printer-Main;192.168.1.200;0;down",
    "Srv-Log;10.0.0.15;105;UP"
]

up_count = 0
server_names = []

for node in nodes:
    parts = node.split(";")
    name = parts[0]
    status = parts[3].strip().lower()
    server_names.append(name)
    if status == "up":
        up_count += 1

print(f"Total servers found: {len(server_names)}")
print(f"Number of servers in UP status: {up_count}")
print("\nServer names:")
for name in server_names:
    print(name)   