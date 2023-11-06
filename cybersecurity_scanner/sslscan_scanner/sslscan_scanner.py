
import sslscan
from sslscan import modules
from sslscan.module.scan import BaseScan

class SSLScanScanner:
    def __init__(self, target):
        self.target = target
        self.scanner = sslscan.Scanner()

    def scan(self):
        self.scanner.scan(self.target)
        for server in self.scanner.get_results():
            for ssl_version in server.accepted_ssl_versions:
                print("Accepted: %s" % ssl_version)
            for ssl_version in server.rejected_ssl_versions:
                print("Rejected: %s" % ssl_version)
            for ssl_version in server.failed_ssl_versions:
                print("Failed: %s" % ssl_version)
