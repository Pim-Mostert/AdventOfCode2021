def ReadData(filePath):
    # open the data file
    file = open(filePath)
    # read the file as a list
    data = file.readlines()
    # close the file
    file.close()

    return [int(line.strip()) for line in data]