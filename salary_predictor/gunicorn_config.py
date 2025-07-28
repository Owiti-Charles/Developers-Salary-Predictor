import multiprocessing

import psutil

# Get system information
CORES = multiprocessing.cpu_count()
TOTAL_MEMORY = psutil.virtual_memory().total / (1024 * 1024 * 1024)  # Memory in GB

# Dynamic worker calculations
# Use more workers if we have more memory, but keep it reasonable
workers_per_core = min(4, TOTAL_MEMORY / (4 * CORES))  # Assume 4GB per worker
worker_count = int(CORES * workers_per_core)

# Ensure we have at least 2 workers and no more than 64
worker_count = max(2, min(worker_count, 64))

bind = "0.0.0.0:5000"
workers = worker_count
worker_class = "gthread"

# Dynamic thread calculation based on CPU cores
# More threads for I/O bound applications, fewer for CPU bound
threads = CORES * 4

# Dynamic connection settings based on available memory
# Assume each connection might use about 400KB of memory
max_memory_connections = int((TOTAL_MEMORY * 1024) / 0.4)  # Convert GB to MB
worker_connections = min(2000, max_memory_connections // worker_count)

# Timeouts and keepalive
timeout = 120
keepalive = 30

# Request recycling to prevent memory leaks
max_requests = 4096
max_requests_jitter = 512

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Performance optimizations
preload_app = True
worker_pre_fork = True
enable_sendfile = True

# Connection queue
backlog = min(2048, max_memory_connections // 2)

# Add graceful timeout
graceful_timeout = 120


# Add some basic status info on startup
def on_starting(server):
    print("Starting Gunicorn with:")
    print(f"* Number of CPU cores: {CORES}")
    print(f"* Total Memory: {TOTAL_MEMORY:.1f}GB")
    print(f"* Workers: {worker_count}")
    print(f"* Threads per worker: {threads}")
    print(f"* Max connections per worker: {worker_connections}")
    print(f"* Max total connections: {worker_connections * worker_count}")
