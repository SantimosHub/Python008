file_name = "March 14/contacts copy.txt"

with open(file_name, "") as file:

    row = file.readlines()[3]
    old_data = file.read()
    print(row)
    # old_data.replace(row, "DDDDDD")

    file.write(old_data.replace(row, "DDDDDD"))
