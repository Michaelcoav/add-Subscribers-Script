"""
Reads the given file, then adds to output Rows to then write to new csv file.

@param string input_File_Name   name of the input csv file.
@return list output_Rows   holding rows of content that will be used to write to new csv file.
"""
def read_SHPE_CSV(input_File_Name):
    # input csv file used to create csv file comptaible for mailchimp adding subscribers
    input_File = open(input_File_Name, "r")

    # used to store student class to graduation years
    student_To_Year = {
          "Freshman": "2026",
          "Sophomore": "2025",
          "Junior": "2024",
          "Senior": "2023"
    }

    # used to store the rows that will be written in the new csv file
    output_Rows = []

    # used to skip header line
    headerLine = True

    for row in input_File:
	    # hold an array that holds all the columns in the excel file on the current row split by commas
        columns = row.split(",")

        # skip header line
        if (headerLine):
            headerLine = False
            continue

        email = columns[3].strip().lower()

        full_Name = columns[1].split(" ")

        first_Name = full_Name[0]

        last_Name = full_Name[1].capitalize()

        major = columns[7].strip().lower()

        student_Class = columns[5]

        grad_Year = student_To_Year.get(student_Class)

        # student class given not in dictionary assume they are a senior
        if (grad_Year == None):
              grad_Year = "Senior"
        
        new_Row = f"\n{email},{first_Name},{last_Name},{major},{grad_Year}"

        output_Rows.append(new_Row)

        

    input_File.close()

    return output_Rows

"""
Creates the new csv file then appends the rows from output rows to the csv file.

@param output_File_Name string  name of the csv file that will be created.
@param ouput_Rows list  list of rows that will be written to new csv file.
@return None
"""
def write_Mailchimp_CSV(output_File_Name, output_Rows):
    # output csv file that will be written to hold the necessary information from input
    output_File = open(output_File_Name, "w")

    # heading for the output csv file
    output_File_Heading = "EmailAddress,FirstName,LastName,Major,GraduationYear"

    output_File.write(output_File_Heading)

    for row in output_Rows:
          output_File.write(row)

    output_File.close()


def main():
    input_File_Name = input("What is the name of the input file? ")
	
    output_File_Name = input("What is the name of the output file? ")

    output_Rows = read_SHPE_CSV(input_File_Name)

    write_Mailchimp_CSV(output_File_Name, output_Rows)

if (__name__ == "__main__"):
	main()