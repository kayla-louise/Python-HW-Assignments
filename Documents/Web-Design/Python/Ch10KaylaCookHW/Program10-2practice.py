# This program reads the contents of the
# philosophers.txt file one line at a time.
def main():
    # Open a file named philosophers.txt.
    infile = open('inputfile#5.dat', 'r')

    # Read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Close the file.
    infile.close()

    # Print the names that were read.
    print('Here are the names of three philosophers:')
    print(line1)
    print(line2)
    print(line3)

# Call the main function.
main()
