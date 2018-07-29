#!/usr/bin/env python3
import conu

backend = conu.DockerBackend()

image_ngix = backend.ImageClass('docker.io/library/nginx')

container_ngix = image_ngix.run_via_binary()
container_ngix.wait_for_port(80)
if container_ngix.is_port_open(80):
    print("******* Run OK")
else:
    print("******* Run FAILED")


# ##################################
# HTTP actions
# ##################################
container_ip = container_ngix.get_IPv4s()[0]

http_session = container_ngix.http_session

response = http_session.get('http://' + container_ip)
print("Status code", response.status_code)
print("HTTP :", response.text)



# ##################################
# FS actions
# ##################################

with container_ngix.mount() as fs:
    if "keepalive_timeout  65;" in fs.read_file("/etc/nginx/nginx.conf"):
        print("******* Run OK")
    else:
        print("******* Run FAILED")

input()
backend.cleanup_images()
backend.cleanup_containers()
