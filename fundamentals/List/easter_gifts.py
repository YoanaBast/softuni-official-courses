# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family.
# First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# · "OutOfStock {gift}"
# o Find the gifts with this name in your collection, if any, and change their values to "None".

# · "Required {gift} {index}"
# o If the index is valid, replace the gift on the given index with the given gift.

# · "JustInCase {gift}"
# o Replace the value of your last gift with this one.

# In the end, print the gifts on a single line, except the ones with the value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
#
# Input / Constraints
# · On the 1st line, you will receive the names of the gifts, separated by a single space.
#
# · On the following lines, until the "No Money" command is received, you will be receiving commands.
#
# · The input will always be valid.
#
# Output
#
# · Print the gifts in the format described above.

gifts_original_list = input().split()

while command != 'No Money':
    temp_list = command.split()

    if 'OutOfStock' in temp_list:
        item = temp_list[1]
        for x in range(len(gifts_original_list)):
            if item in gifts_original_list:
                gifts_original_list[x] = gifts_original_list[x].replace(item, 'None')

    if "Required" in temp_list:
        index = int(temp_list[2])

        if 0 <= index < len(gifts_original_list):
            gifts_original_list[index] = temp_list[1]
        else:
            gifts_original_list.append(temp_list[1])

    if 'JustInCase' in temp_list:
        gifts_original_list[-1] = temp_list[1]

    command = input()

for y in range(len(gifts_original_list) -1, -1, -1):
    if gifts_original_list[y] == 'None':
        gifts_original_list.pop(y)

print(*gifts_original_list, sep=' ')
