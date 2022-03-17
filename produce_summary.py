'''inputs a daily file and returns the delivery summary'''
def generate_summary(the_file):
    for line in the_file:
        line = line.rstrip()##removes spaces to the right
        words = line.split('|')##makes a list of each item in the listed

        ##confirms each section into a solo variable. unnecessary
        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")

print("Day 1")
the_file = open("um-deliveries-day-1.txt")
##filled with lines of - Mellon|Count|Amount
generate_summary(the_file)
the_file.close()


print("Day 2")
the_file = open("um-deliveries-day-2.txt")
generate_summary(the_file)
the_file.close()


print("Day 3")
the_file = open("um-deliveries-day-3.txt")
generate_summary(the_file)
the_file.close()