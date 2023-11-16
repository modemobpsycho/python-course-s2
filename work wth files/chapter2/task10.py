def read_csv():
    with open("data.csv", encoding="utf-8") as file:
        key = [line.strip() for line in file.readline().split(",")]
        value = [line.strip().split(',') for line in file.readlines()]
    return [dict(zip(key, i)) for i in value]
