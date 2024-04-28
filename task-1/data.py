

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file: # read the file
            total_salary = 0 
            total_person = 0
            for line in file:
                _, salary = line.strip().split(",") # define salary from line
                total_salary += int(salary)
                total_person += 1
            average_salary = total_salary / total_person # count averege salary 
            return float(total_salary), float(average_salary)
    except FileNotFoundError:
        raise FileNotFoundError ("File not found")
    except Exception as e:
        raise Exception (e)
    
