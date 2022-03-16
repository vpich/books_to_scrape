import csv
from variables import data_dict


with open("data.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(data_dict)
    writer.writerow(data_dict.values())


if __name__ == "__main__":
    # print(header_titles)
    print(data_dict)
