def volume(a):
    '''
    Returns the volume of a cube given the length of one of its sides.

	Parameters:
		a (int): A positive decimal integer representing the side length

	Returns:
		(int): Returns the volume of the cube if the input is valid. If the
               input is not valid (i.e., not a positive integer), the function
               returns -1.
    '''
    try:
        # Convert input to int
        a_converted = int(a)

        # Return unsuccessfully if input is not a positive integer
        if a_converted <= 0:
            return -1
        # Return the cubed input
        else:
            return a_converted**3
    # Return unsuccessfully if input is not an integer
    except ValueError:
        return -1
