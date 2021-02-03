def list_avg(lst):
    '''
    Returns the average value of a list of integers.

	Parameters:
		lst (int[]): A list of integers to be averaged

	Returns:
		(int): Returns the average value of the list if it has at least one
               element and all elements are integers. If the input is not valid
               (i.e., one or more elements are not integers), the function
               returns -1.
    '''
    # Return unsuccessfully if list is empty
    if len(lst) == 0:
        return -1
    # Return first element if it is the only one in the list
    elif len(lst) == 1:
        return lst[0]
    else:
        lst_sum = 0
        # Iterative over list and sum elements
        for num in lst:
            try:
                # Convert element to int
                num_converted = int(num)
                # Add current element to the sum of all elements in the list
                lst_sum += num_converted
            # Return unsuccessfully if element is not an integer
            except ValueError:
                return -1

        return lst_sum / len(lst)
