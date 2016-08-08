#Kayla Cook
#10-8
#Sales Report

def main():
    """#open inputfile#8.dat file
    inputFile = open('inputfile#8.dat', 'r')

    #read the first field from the first record
    idNum = inputFile.readline()

    #read amount of a sale"""

    #initalize/declare an accumulator
    total = 0.0

    #exception handling
    try:
        #open inputfile#8.dat file
        infile = open('inputfile#8.dat', 'r')
        #read values and calculate total
        for line in infile:
            amount = float(line)
            total = total + amount

        #close the file
        infile.close()

        #print the totals
        print(format(total, ',.2f'))
    except Exception as err:
        print(err)

#call main
main()
