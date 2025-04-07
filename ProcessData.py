#ProcessData.py
#Name: Arturo
#Date: 4/6/2025
#Assignment: Lab 08

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')


  #Process each line of the input file and output to the CSV file
  
  #line = inFile.readline()

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum)
    year_short = YearAbbr(year)
    major_abbr = major[0] + major[1] + major[2]
    major_year = major_abbr + "-" + year_short
    
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)
    print(student_id)  

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()


def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]

  #print(id)
  return id

def YearAbbr(year):
    if year == "Freshman":
      year_short = "FR"
    elif year == "Sophomore":
      year_short = "SO"
    elif year == "Junior":
      year_short = "JR"
    elif year == "Senior":
      year_short = "SR"
  
    return year_short


if __name__ == '__main__':
  main()
