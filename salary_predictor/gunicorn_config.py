import multiprocessing

workers_per_core = 2.5
worker_count = int(multiprocessing.cpu_count() * workers_per_core)

bind = "0.0.0.0:8000"
worker_class = "gthread"
threads = multiprocessing.cpu_count() * 4
worker_connections = 2000
timeout = 60
keepalive = 5

max_requests = 4096
max_requests_jitter = 512

accesslog = "-"
errorlog = "-"
loglevel = "info"

preload_app = True
worker_pre_fork = True
enable_sendfile = True

backlog = 2048
