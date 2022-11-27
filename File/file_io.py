# temp_file = open("temp.txt", "w")
print("we are paragons", file=temp_file)
print("we are from semicolon africa", file=temp_file)
temp_file.close()
input_file = open("temp.txt", "r")
output_file = open("output.txt", "w")

for line_str in input_file:
    new_str = ''
    # todo get rid of carriage return
    line_str = line_str.strip()
    for char in line_str:
        # todo concat at the left (reverse)
        new_str = char + new_str
    #     print to output_file
    print(new_str, file=output_file)

    # todo   include a print to shell so we can observe progress
    print('Line: {:12s} reversed is: {:s}'.format(line_str, new_str))
input_file.close()
output_file.close()
