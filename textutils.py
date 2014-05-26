def replace(str, remove_list):
    for ch in remove_list:
        str = str.replace(ch, '')
    return str