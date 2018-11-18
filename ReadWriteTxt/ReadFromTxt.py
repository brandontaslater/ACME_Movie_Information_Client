def read_from_txt(path):
    list = []
    with open(path, "r") as ins:
        for line in ins:
            list.append(line.split('|'))
    print(len(list))
    return list


def get_record_number(path):
    data = read_from_txt(path)
    print(len(data)-1)
    print((data[len(data)-1][0]))
    print("Recordno")

    return data[len(data)-1][0]
