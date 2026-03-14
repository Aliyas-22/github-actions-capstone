import psutil
def get_system_metrics():

    """
    this api will get the system matrics like cpu , ram , disk usage
    """
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent= psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    cpu_threshold = 10
    if cpu_percent > cpu_threshold:
        cpu_status = "High CPU Usage"
    else:
        cpu_status = "healthy"
    return {
        "cpu_percentage": cpu_percent,
        "menmory_percentage": memory_percent,
        "disk_percentage": disk_percent,
        "cpu_threshold": cpu_threshold,
        "system_health": cpu_status
    }