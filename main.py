import psutil
import time
import os
from datetime import datetime

THRESHOLDS = {
    'cpu_percent': 80.0,
    'memory_percent': 85.0,
    'disk_percent': 90.0
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_system_status():
    return {
        'cpu': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'timestamp': datetime.now().strftime("%H:%M:%S")
    }

def monitor():
    try:
        while True:
            status = get_system_status()
            clear_screen()
            
            print(f"--- System Health Dashboard [{status['timestamp']}] ---")
            
            for resource, value in status.items():
                if resource == 'timestamp': continue
                
                threshold_key = f"{resource}_percent"
                alert = ""
                if value > THRESHOLDS.get(threshold_key, 100):
                    alert = "CRITICAL: THRESHOLD EXCEEDED!"
                
                print(f"{resource.upper()}: {value}% {alert}")
            
            print("\nMonitoring active. Refreshing every 5 seconds... (Ctrl+C to stop)")
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nMonitor Stopped.")

if __name__ == "__main__":
    monitor()
