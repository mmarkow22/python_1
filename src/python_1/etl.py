import requests
import decimal
from decimal import Decimal

from decorators import time_measure


class RetrievalError(Exception):
    pass


class NotFoundError(RetrievalError):
    pass


class AccessDeniedError(RetrievalError):
    pass


class Etl:
    @time_measure
    def get_file_from_url(self, url, name="latest.csv"):
        response = requests.get(url)
        if response.status_code == 200:
            with open(name, 'wb') as file:
                file.write(response.content)
        elif response.status_code == 404:
            raise NotFoundError(f"File not found: {url}")
        elif response.status_code == 403:
            raise AccessDeniedError(f"Access denied: {url}")
        else:
            raise RetrievalError(f"Failed to retrieve file from {url}, status code: {response.status_code}")
    
    @time_measure
    def read_file_line(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()

    @time_measure
    def count_line_statistics(self, lines):
        decimal.getcontext().rounding = decimal.ROUND_HALF_UP
        for line in lines: 
            words = line.split(',') 
            values = [Decimal(value) for value in words[1:] if value != '-'] # Skip the first column and missing values
            missing_indexes = [i for i in range(len(words)) if words[i] == '-']
            sum_result = sum(values)
            average = round(sum_result / len(values), 3)
            yield [sum_result, average, missing_indexes]

    @time_measure
    def save_statistics_to_files(self, statistics, statics_file, missing_values_file):
        with open(statics_file, 'w') as statics_file, open(missing_values_file, 'w') as missing_values_file:
            index = 1
            for stats in statistics:
                statics_file.write(f"{index},{stats[0]},{stats[1]}\n")
                missing_values_file.write(f"{index},{stats[2]}\n")
                index += 1