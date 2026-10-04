 #1 importing 
import csv
import json
from typing import Callable, Tuple, Dict,List,Any
from datetime import datetime
import statistics

# 2.loading 

def load_csv(path : str)-> list[dict[str , str]]:
    with open(path, "r" ,newline = "", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data

# 3q.filter rows

def filter_rows(data: List[Dict[str, str]],
             column: str, 
             predicate: Callable[[str], bool]) -> List[Dict[str, str]]:

   filtered_data =[]

   for row in data:
      
       if predicate(row.get(column , "")):
          filtered_data.append(row)


   return filtered_data

data = load_csv("students.csv")

filtered_data = filter_rows(
    data,
     "Department",
     lambda x: x == "Data Science"
)

print(filtered_data)

#4.Implement column_stats()

def column_stats(data: 
             List[Dict[str, str]], 
             column: str) -> Tuple[float, float, int]:
    
    values =  []

    for row in data:

        try:
           number=float(row[column])
           values.append(number)

        except (ValueError,KeyError):
            continue

    if len(values) == 0:
        return 0.0,0.0,0

    mean_value = statistics.mean(values)
    median_value = statistics.median(values)
    count = len(values)

    return mean_value ,median_value,count

#5.Implement a function write_json

def write_json(data: Any, path: str) -> None:

    with open(path , "w",encoding="utf-8")as  file:

        json.dump(data, file, indent=2)

#6.Implement a simple logger class 

class SimpleLogger:

    def __init__(self, filename="app.log"):
        self.filename = filename

    def _write_log(self, level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.filename, "a", encoding="utf-8") as file:

            file.write(f"{timestamp} - {level} - {message}\n")

    def info(self, message: str):
        self._write_log("INFO", message)

    def warning(self, message: str):
        self._write_log("WARNING", message)

    def error(self, message: str):
        self._write_log("ERROR", message)

 #7Q add main workflow

if __name__ == "__main__":

    logger = SimpleLogger()

    try:
        logger.info("Program started")

        data = load_csv("students.csv")
        logger.info("CSV loaded successfully")

        filtered_data = filter_rows(
            data,
            "Department",
            lambda x: x == "Data Science"
        )

        logger.info("Filtering completed")

        mean_value, median_value, count = column_stats(
            data,
            "Marks"
        )

        logger.info("Statistics calculated")

        write_json(filtered_data, "filtered_data.json")

        logger.info("JSON file created")

        print("Mean:", mean_value)
        print("Median:", median_value)
        print("Count:", count)

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")






