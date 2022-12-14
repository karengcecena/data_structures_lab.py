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

# print(get_villagers_by_species("villagers.csv", search_string = "Alligator"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    
    filename = open(filename)


    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []
    

    for each_line in filename:
        each_line = each_line.split("|")

        if each_line[3] == "Fitness":
            fitness.append(each_line[0])

        elif each_line[3] == "Nature":
            nature.append(each_line[0])

        elif each_line[3] == "Education":
            education.append(each_line[0])

        elif each_line[3] == "Music":
            music.append(each_line[0])

        elif each_line[3] == "Fashion":
            fashion.append(each_line[0])

        elif each_line[3] == "Play":
            play.append(each_line[0])

    fitness = sorted(fitness)
    nature = sorted(nature)
    education = sorted(education)
    music = sorted(music)
    fashion = sorted(fashion)
    play = sorted(play)
    

    names_and_hobbies = [fitness] + [nature] + [education] + [music] + [fashion] + [play]


    return [names_and_hobbies]

# print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    filename = open(filename)
    
    all_data = []

    for each_line in filename:
        each_line = each_line.split("|")

        all_data.append((each_line[0], each_line[1], each_line[2], each_line[3], each_line[4]))


    return all_data

# print(all_data("villagers.csv"))


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

    filename = open(filename)
    
    for each_line in filename:
        each_line = each_line.split("|")
        
        if villager_name == each_line[0]:
            
            motto = each_line[4]
            return motto


# print(find_motto("villagers.csv", "Deli"))


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

    filename = open(filename)

    villagers_alike = []

    villager_personality = ""
    
    new_list = []
    
    # Get personality type:     
    for each_line in filename:
        each_line = each_line.split("|")
        new_list.append(each_line)

        if villager_name == each_line[0]:
            villager_personality = each_line[2]

    # Iterate through new_list instead........ 
    for each_line in new_list:
        if villager_personality == each_line[2] and each_line[0] != villager_name:
            villagers_alike.append(each_line[0])


    return set(villagers_alike)

print(find_likeminded_villagers('villagers.csv', 'Wendy'))