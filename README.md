# Real-Time System Health Monitor

A lightweight, automated monitoring agent designed to track hardware performance and trigger alerts when system resources exceed predefined thresholds.

## Features
- **Live Dashboard**: Provides a real-time terminal interface displaying CPU, RAM, and Disk usage.
- **Automated Alerting**: Features threshold-based logic to flag critical resource exhaustion (e.g., CPU > 80%).
- **Low Overhead**: Built using the `psutil` library for high-efficiency system polling with minimal CPU footprint.
- **Cross-Platform**: Compatible with Windows (PowerShell/CMD) and Linux/macOS terminals.

## Technical Deep-Dive
- **Resource Polling**: Utilizes non-blocking system calls via `psutil` to gather hardware metrics without hanging the application.
- **Dynamic Terminal UI**: Implemented an automated "Clear-and-Redraw" cycle to simulate a live dashboard experience in a CLI environment.
- **Error Handling**: Uses `KeyboardInterrupt` handling for a clean exit, ensuring system resources are released properly.

## Prerequisites
- Python 3.x
- `psutil` library

## Installation & Usage
1. **Clone the repository** or download `main.py`.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application**:
   ```bash
   python main.py
   ```
