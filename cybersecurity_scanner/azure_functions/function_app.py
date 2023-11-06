

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    scanner_type = req.params.get('scanner')

    if not scanner_type:
        return func.HttpResponse(
             "Please pass a scanner type (openvas or sslscan) on the query string",
             status_code=400
        )

    if scanner_type == 'openvas':
        from openvas_scanner.openvas_scanner import OpenvasScanner
        scanner = OpenvasScanner()
    elif scanner_type == 'sslscan':
        from sslscan_scanner.sslscan_scanner import SSLScanScanner
        scanner = SSLScanScanner()
    else:
        return func.HttpResponse(
             "Invalid scanner type. Please use 'openvas' or 'sslscan'",
             status_code=400
        )

    result = scanner.scan()

    return func.HttpResponse(str(result))
