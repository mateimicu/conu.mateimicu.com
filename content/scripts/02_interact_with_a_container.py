#!/usr/bin/env python3
import conu

backend = conu.DockerBackend()

# bash image
image_bash = backend.ImageClass('docker.io/library/bash')

container_bash = image_bash.run_via_binary(command=["echo", "Hello Python Mambu Labs"])

if "Mambu Labs" in container_bash.logs_unicode():
    print("******* Run OK")
else:
    print("******* Run FAILED")

# wait for the container to finish
exit_code = container_bash.wait()
if exit_code['StatusCode'] == 0:
    print("******* Run OK")
else:
    print("******* Run FAILED")

# ##################################
# Tests for nginx
# ##################################
image_ngix = backend.ImageClass('docker.io/library/nginx')

container_ngix = image_ngix.run_via_binary()
container_ngix.wait_for_port(80)
if container_ngix.is_port_open(80):
    print("******* Run OK")
else:
    print("******* Run FAILED")



input()
backend.cleanup_images()
backend.cleanup_containers()
