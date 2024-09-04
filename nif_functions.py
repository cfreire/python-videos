def convert_txt_to_list(file_name: str) -> list:
    """ Converts a txt file to a list """

  
    with open(file_name) as file:
        nif_list = [line.strip().split() for  line in file]
        flat_list = [item for sublist in nif_list for item in sublist]
    return flat_list

