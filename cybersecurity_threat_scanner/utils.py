```python
import subprocess
import os

def run_openvas_scan(target):
    """
    Function to run OpenVAS scan on a target
    """
    command = ["openvas", "-T", target]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        raise Exception(f"Error occurred while running OpenVAS scan: {error}")

    return output.decode('utf-8')

def run_sslscan(target):
    """
    Function to run SSLScan on a target
    """
    command = ["sslscan", target]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        raise Exception(f"Error occurred while running SSLScan: {error}")

    return output.decode('utf-8')

def scan_target(target):
    """
    Function to run both OpenVAS and SSLScan on a target
    """
    openvas_result = run_openvas_scan(target)
    sslscan_result = run_sslscan(target)

    return {
        "openvas": openvas_result,
        "sslscan": sslscan_result
    }
```