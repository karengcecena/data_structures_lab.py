"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    filename = open(filename)
    species = []
    
    for each_line in filename:
        each_line = each_line.split("|")
        species.append(each_line[1])
        
    species = set(species)

    return species


# print(all_species("villagers.csv"))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    filename = open(filename)
    villagers = []

    for each_line in filename:
        each_line = each_line.split("|")
        
        if search_string == each_line[1]:
            villagers.append(each_line[0])


    return sorted(villagers)

print(get_villagers_by_species("villagers.csv", search_string = "Alligator"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    filename = open(filename)

    for each_line in filename:
        each_line = each_line.split("|")

        # Return a list of lists containing villagers' names, grouped by hobby

    hobby = each_line[3]
    villagers = []

    for hobby in each_line:
        if hobby == "Education"
            return each_line[0]
        

    ###### karen: 
    filename = open(filename)
    villagers = []

    for each_line in filename:
        each_line = each_line.split("|")

        # Return a list of lists containing villagers' names, grouped by hobby

        # ex: hobby = [names1, name 2, name]
        hobbies = []
        hobbies = set(hobbies)
        hobbies = list(hobbies)

        names_and_hobbies = []

        for each_line[3] in each_line:
            hobbies.append(each_line[3])

        for each_line in filename:
            i = 0
            j = 0
            
            if each_line[3] == hobbies[i]:
                names_and_hobbies.append(hobbies[i] = [])
                names_and_hobbies[i][j].append(each_line[0])

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
