
from etl import Etl

etl = Etl()

etl.get_file_from_url("https://oleksandr-fedoruk.com/wp-content/uploads/2025/10/sample.csv", "latest.csv")

etl.save_statistics_to_files(
    etl.count_line_statistics(
        etl.read_file_line("latest.csv")), 
        statics_file = "values.csv", 
        missing_values_file = "missing_values.csv")