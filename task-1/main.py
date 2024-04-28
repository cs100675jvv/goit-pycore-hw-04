from data import total_salary # import total_salary function


def main():
    total, average = total_salary("task-1/salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



if __name__ == "__main__":
    main()