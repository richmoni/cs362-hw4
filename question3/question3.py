def full_name(fname, lname):
    '''
    Returns a full name given a first and last name.

	Parameters:
		fname (str): A string representing the first name
		lname (str): A string representing the last name

	Returns:
		(str): Returns the concatenation of first and last names without
               leading or trailing whitespace characters.
    '''
    if lname == "":
        return fname
    if fname == "" and lname != "":
        return lname
    else:
        return f"{fname} {lname}"
