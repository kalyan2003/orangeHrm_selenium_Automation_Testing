@echo off
call C:\Users\pavan\Documents\Selenium_Projects\nopCommerce_Project\.venv\Scripts\activate.bat
pytest -s -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome

pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome

