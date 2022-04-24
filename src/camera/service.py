import uuid

from pathlib import Path

from django.conf import settings
from django.core.files import File

from utils.report_utils import GenerateReport


def convert_camera_parameters(data):
    string = ''
    for parameter in data.values():
        string = f'{string} {parameter}'

    return string


def create_many_test_parameters(string, limit=50):
    new_string = ''
    for _ in range(limit+1):
        new_string += f'{string}\n'
    return new_string


def create_report_xlsx(data):
    file_path = f'{settings.MEDIA_ROOT}/temp-reports/report_{uuid.uuid4()}.xlsx'
    report = GenerateReport(file_path)
    report.generate_report(data)

    path = Path(file_path)
    f = path.open(mode='rb')
    django_file = File(f, name=path.name)

    return django_file, file_path
