out_file = open("name_storage.txt", 'w')

your_name = str(input("Please enter your name: "))

print("Your name is {0}".format(your_name), file=out_file)

out_file.close()
sum_numbers = 0

number_file = open("numbers.txt", 'r')
for line in number_file:
    sum_numbers = sum_numbers + int(line)


print(sum_numbers)
