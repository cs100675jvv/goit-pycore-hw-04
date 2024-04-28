

def get_cats_info(path):
    cat_list = []
    try:
        with open(path, "r", encoding="utf-8") as file: # read the file
            for line in file:
                cat_id, cat_name, cat_age = line.strip().split(",") # extract data from line
                cat_list.append({
                    "id": cat_id,
                    "name": cat_name,
                    "age": cat_age
                })
            return cat_list


    except FileNotFoundError: 
        raise FileNotFoundError ("File not found")
    except Exception as e:
        raise Exception (e)
    
