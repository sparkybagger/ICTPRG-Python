
def PrintBoxByWidth():
    rows = 5
    columns = 60

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if(i == 1 or i == rows or j == 1 or j == columns):
                print("x", end='')
            elif(i == 2 or i == 4):
                print(" ", end='')
            else:
                print("o", end='')
        print("")
PrintBoxByWidth()