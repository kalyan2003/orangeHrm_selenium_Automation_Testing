import os
import logging

class logFileGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger("automationLogger")

        # Avoid adding multiple handlers on repeated test runs
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            log_path = r"C:\Users\pavan\Documents\Selenium_Projects\nopCommerce_Project\Logs"
            os.makedirs(log_path, exist_ok=True)  # Ensure the directory exists

            file_handler = logging.FileHandler(os.path.join(log_path, "automation.log"), mode='a')
            formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s", "%Y-%m-%d %I:%M:%S %p")
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger