#!/usr/bin/env python3

import conu

backend = conu.DockerBackend()

image_ngix = backend.ImageClass('docker.io/library/nginx')

container = image_ngix.run_via_binary()

input()
backend.cleanup_images()
backend.cleanup_containers()
