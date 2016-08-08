# This program writes three lines of data
# to a file.
def main():
    # Open a file named philosophers.txt.
    outfile = open('numbers.dat', 'w')

    # Write the names of three philosphers
    # to the file.
    outfile.write(str(10) + '\n')
    outfile.write(str(20) + '\n')
    outfile.write(str(30) + '\n')

    # Close the file.
    outfile.close()

# Call the main function.
main()
