server_name = "nginx"
server_port = 8080

server_one = {
    "name": server_name, 
    "port":server_port
}


servers = [server_one]

def register_server(name, port):
    new_server = {
        "name": name, 
        "port": port
    }
    servers.append(new_server)

    return new_server


register_server("redis", 6379)
register_server("postgres", 5432)

print(servers)