import re
fname = 'data_list.txt'
fhand = open(fname, 'r')
phone_numbers = list()
for line in fhand:
    line = line.rstrip()
    #print(line)
    if re.match(r"^\d.*-\d.*-\d.*", line):
        print('extracted phone number', line)
        phone_numbers.append(line)
print('Final list of phone numbers is', phone_numbers)