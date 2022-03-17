'''inputs a daily file and returns the delivery summary'''
def generate_summary(day,the_file):
    '''reaches out into a daily file'''
    print(f"Day ", day)
    ## opens the file and makes it a giant string
    delivery_log = open(the_file)

    for line in delivery_log:
        line = line.rstrip()##removes spaces to the right
        words = line.split('|')##makes a list of each item in the listed

        ##confirms each section into a solo variable. unnecessary except for clarity
        melon, count, amount = words

        print(f"Delivered {count} {melon}s for total of ${amount}")
    
    delivery_log.close()

##each file filled with lines of - Mellon|Count|Amount
generate_summary(1,"um-deliveries-day-1.txt")
generate_summary(2,"um-deliveries-day-1.txt")
generate_summary(3,"um-deliveries-day-1.txt")