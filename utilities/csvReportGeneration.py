import csv
from datetime import datetime


def write_result_to_csv(test_id, class_name, status ):
    file_path = r"C:\Users\pavan\Documents\Selenium_Projects\nopCommerce_Project\reports\csv_report.csv"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, class_name, test_id, status])
