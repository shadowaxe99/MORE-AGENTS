```python
import os
from azure.functions import HttpRequest, HttpResponse
from utils import run_sslscan, run_openvas

def main(req: HttpRequest) -> HttpResponse:
    target = req.params.get('target')

    if not target:
        return func.HttpResponse(
             "Please pass a target on the query string or in the request body",
             status_code=400
        )

    ssl_results = run_sslscan(target)
    openvas_results = run_openvas(target)

    return func.HttpResponse(f"Scan results:\nSSL Scan:\n{ssl_results}\nOpenVAS Scan:\n{openvas_results}")
```