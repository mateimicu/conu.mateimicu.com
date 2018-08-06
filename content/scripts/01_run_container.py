#!/usr/bin/env python3

import conu

backend = conu.DockerBackend()

image_nginx = backend.ImageClass('docker.io/library/nginx')

container = image_nginx.run_via_binary()

input()
backend.cleanup_images()
backend.cleanup_containers()
