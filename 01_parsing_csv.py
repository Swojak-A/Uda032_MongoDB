# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = "files"
DATAFILE = "beatles-discography.csv"


def parse_file(datafile):
    data = []
    with open(datafile, "r") as fp:
        header = fp.readline().split(",")

        n = 0
        for line in fp:
            if n >= 10:
                break

            output_dict = {}
            for label, item in zip(header, line.split(",")):
                output_dict[label.strip()] = item.strip()

            # print(output_dict)
            data.append(output_dict)

            n += 1



    return data


def test(datafile):
    # a simple test of your implemetation
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)',
                 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum',
                 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964',
                 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    try:
        assert d[0] == firstline
        assert d[9] == tenthline
        print("Success!!!")
    except AssertionError:
        print("Not Good...")

if __name__ == "__main__":
    full_path = (os.path.join(DATADIR, DATAFILE))

    test(full_path)