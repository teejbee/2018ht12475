
# Assignment for SSZG519 - DSA
# By Balaji Thope Janakiram '2018ht12475@wilp.bits-pilani.ac.in'
def main():
    n = int(raw_input('Enter the number of trains: '))
    # For calculating the number of platforms required, we don't need to store
    # the train names. Any negative integer for number of trains is considered
    # as no trains.
    # schedule stores array of two-tuple (arrival, departure)
    schedule = []
    for train in range(1,n+1):
        arr = raw_input('Enter arrival of train {} in HHMM : '.format(train))
        dep = raw_input('Enter departure of train {} in HHMM : '.format(train))
        
        #sanitary checks
        arr = str(arr)
        arr = arr[:4]
        assert str.isdigit(arr), 'Arrival time has to be in HHMM format'
        assert int(arr[0:2]) < 24 and int(arr[2:4]) < 60, 'Invalid HHMM format'
        dep = str(dep)
        dep = dep[:4]
        assert str.isdigit(dep), 'Departure time has to be in HHMM format'
        # assert dep > arr, 'Arrival has to be earlier than departure'
        if dep < arr:
            # The train is staying overnight i.e, past 0000hrs
            print 'Train {} is staying overnight'.format(train)
            dep = str(int(dep[0:2])+24) + dep[2:4]
        
        schedule.append((arr,dep))
 
    print_min_pf(schedule)

def print_min_pf(schedule):
    '''
        Main algorithm to calculate and print the number of platforms for the 
        given schedule. The array of input tuples are stored in another array 
        by splitting the arrival and departure and having them as first 
        element of the tuple and +1/-1 as second element of the tuple in case
        of arrival / departure respectively.
        
        eg) schedule = [('0900', '0930'), ('0915', '1300'), 
                        ('1030', '1100'), ('1045', '1145')]
    '''
    merged_schedule = []
    print schedule
    for train in schedule:
        # arrival is in [0] and denoted by +1
        merged_schedule.append((train[0], 1))
        # departure is in [1] and denoted by -1
        merged_schedule.append((train[1], -1))

    # sort based on first element in tuple, which is the time
    merged_schedule.sort()

    plat_sum = 0 # variable to store cumulative sum
    min_plat = 0 # variable to store max of cumulative sum

    # find the cumulative of second element in the tuple
    for train in merged_schedule:
        plat_sum += train[1]
        min_plat = max(min_plat, plat_sum)
    
    print('The schedule requires at least {} platform(s) '
            'to accomodate all trains'.format(min_plat))
    
if __name__ == '__main__':
    main()

