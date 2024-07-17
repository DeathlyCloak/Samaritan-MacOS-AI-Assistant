"""
System Monitor Module
"""

import psutil

class SystemMonitor:
    def get_cpu_usage(self):
        return psutil.cpu_percent()

    def get_battery_status(self):
        battery = psutil.sensors_battery()
        return battery.percent
