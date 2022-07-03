total = 0
outfile = open('numberout.txt','w')

with open('numberin.txt','r') as fin:
    for line in fin:
        try:
            total+=float(line)
            outfile.write(line)
        except ValueError:
            print(line+"is not a number.")
print("Total of all numbers:",format(total, '.2f'),end='')

outfile.close()
