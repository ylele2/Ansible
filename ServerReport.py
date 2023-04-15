import psutil
import socket

# Fetch server details using psutil and socket libraries
hostname = socket.gethostname()
cpu_count = psutil.cpu_count()
cpu_percent = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')

# Generate HTML report
html_report = f"""
<html>
<head>
    <title>Server Details</title>
</head>
<body>
    <h1>Server Details</h1>
    <table>
        <tr>
            <td><b>Hostname:</b></td>
            <td>{hostname}</td>
        </tr>
        <tr>
            <td><b>CPU Count:</b></td>
            <td>{cpu_count}</td>
        </tr>
        <tr>
            <td><b>CPU Percent:</b></td>
            <td>{cpu_percent}%</td>
        </tr>
        <tr>
            <td><b>Memory Info:</b></td>
            <td>Total: {memory_info.total} bytes, Available: {memory_info.available} bytes, Used: {memory_info.used} bytes</td>
        </tr>
        <tr>
            <td><b>Disk Usage:</b></td>
            <td>Total: {disk_usage.total} bytes, Used: {disk_usage.used} bytes, Free: {disk_usage.free} bytes</td>
        </tr>
    </table>
</body>
</html>
"""

# Save the HTML report to a file
with open('/tmp/server_details.html', 'w') as f:
    f.write(html_report)
