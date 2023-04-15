import psutil
import socket
import matplotlib.pyplot as plt

# Fetch server details using psutil and socket libraries
hostname = socket.gethostname()
cpu_count = psutil.cpu_count()
cpu_percent = psutil.cpu_percent(interval=1)
memory_info = psutil.virtual_memory()
disk_usage = psutil.disk_usage('/')

# Generate HTML report with graphical representations
html_report = f"""
<html>
<head>
    <title>Server Details</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
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
    <h2>CPU Usage</h2>
    <div id="cpu-usage"></div>
    <h2>Memory Usage</h2>
    <div id="memory-usage"></div>
    <h2>Disk Usage</h2>
    <div id="disk-usage"></div>
    <script>
        // Create CPU usage chart
        Plotly.newPlot('cpu-usage', [{
            x: ['CPU'],
            y: [{cpu_percent}],
            type: 'bar',
            marker: {{
                color: 'rgb(50, 171, 96)',
                opacity: 0.7
            }}
        }]);

        // Create memory usage chart
        Plotly.newPlot('memory-usage', [{
            x: ['Total', 'Available', 'Used'],
            y: [{memory_info.total}, {memory_info.available}, {memory_info.used}],
            type: 'bar',
            marker: {{
                color: 'rgb(128, 0, 128)',
                opacity: 0.7
            }}
        }]);

        // Create disk usage chart
        Plotly.newPlot('disk-usage', [{
            x: ['Total', 'Used', 'Free'],
            y: [{disk_usage.total}, {disk_usage.used}, {disk_usage.free}],
            type: 'bar',
            marker: {{
                color: 'rgb(255, 165, 0)',
                opacity: 0.7
            }}
        }]);
    </script>
</body>
</html>
"""

# Save the HTML report to a file
with open('/tmp/server_details.html', 'w') as f:
    f.write(html_report)
