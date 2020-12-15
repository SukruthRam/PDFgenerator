import sys
from fpdf import FPDF
import os
import pathlib


def main(file1, file2):

    try:
        with open(file1) as fp:
            data = fp.read()
        fp.close()
    except IOError:
        print('File1 not found')
        print(file1)
        print("The first input file name %s" % file1)
        return False

    try:
        with open(file2) as fp:
            data2 = fp.read()
        fp.close()
    except IOError:
        print('File2 not found')
        return False

    data += " \n "
    data += data2

    x = data.split("\n")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    for i in x:
        pdf.cell(0, 10, i , 0, 1)
    pdf.output('uniqueoutput.pdf', 'F')
    print("output file path is %s" % os.path.abspath('uniqueoutput.pdf'))
    return True



if __name__ == "__main__":
    #base_dir = pathlib.Path().absolute()
    #base_directory = str(base_dir)
    #print(os.path.abspath(sys.argv[1]))
    #print(sys.argv[1])
    #print(sys.argv[2])
    #print("The first input file name %s" % base_directory+'\\'+sys.argv[1])
    #print("The second input file name %s" % base_directory+'\\'+sys.argv[2])
    ret = main("input-1.txt", "input-2.txt")
    if(ret):
        print("File creation successful")
    elif(not ret):
        print("File creation not successful")
	