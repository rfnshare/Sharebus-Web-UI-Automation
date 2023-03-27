import subprocess
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Resources.ExcelUtils import read_configuration_data_from_excel
from Resources.GeneralUtils import read_date, read_time, get_html_reports
from Resources.MailUtils import send_report

configuration_data = read_configuration_data_from_excel("./Test/TestData/test_data.xlsx")

report_file_name_prefix = f"{read_date()}_{read_time()}"
test_type = "regression"
run_command = f"pytest --html=./Reports/HTMLReports/{test_type}_{report_file_name_prefix}_report.html -v " \
              f"--junitxml=./Reports/XMLReports/{test_type}_{report_file_name_prefix}_report.xml" \
              f"-s --alluredir=./Reports/AllureReports/{test_type}_report_allure/{report_file_name_prefix}"

subprocess.run(run_command, shell=True)

# send report if generated
html_reports = get_html_reports(test_type)

# send report to receivers email
project_name = configuration_data["project_name"]
report_receiver_email = configuration_data["report_receiver"]
# send_report(report_receiver_email, html_reports, project_name)

# allure report serve
allure_serve_command = f"allure serve ./Reports/AllureReports/{test_type}_report_allure/{report_file_name_prefix}"

subprocess.run(allure_serve_command, shell=True)
