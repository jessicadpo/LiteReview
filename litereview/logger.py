"""Module for logging unit tests"""
import datetime


class Logger:
    """
    Logger for unit tests (from Prof. Brunet's GitHub code
    (https://github.com/Carleton-BIT/unit-and-integration-testing-example/
    blob/fix-tests/calculator/logger.py)
    """
    def __init__(self):
        self.logs = []

    def log_message(self, message):
        """Create a timestamped log message"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(f"{timestamp} - {message}")

    def get_last_log(self):
        """Get the last log"""
        if self.logs:
            return self.logs[-1]
        return None

    def display_logs(self):
        """Display all logs"""
        for log_entry in self.logs:
            print(log_entry)
