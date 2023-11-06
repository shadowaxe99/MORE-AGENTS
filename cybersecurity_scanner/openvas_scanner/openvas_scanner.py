
import os
from openvas.omplib import OMPv7

class OpenVasScanner:
    def __init__(self):
        self.host = os.getenv('OPENVAS_HOST')
        self.port = os.getenv('OPENVAS_PORT')
        self.username = os.getenv('OPENVAS_USERNAME')
        self.password = os.getenv('OPENVAS_PASSWORD')
        self.omp = OMPv7(self.host, self.username, self.password)

    def scan(self, target):
        config_id = self.omp.config_list[0].get('id')
        target_id = self.omp.create_target(target)
        task_id = self.omp.create_task(target, config_id)
        self.omp.start_task(task_id)
        return task_id

    def get_results(self, task_id):
        return self.omp.get_results(task_id)
