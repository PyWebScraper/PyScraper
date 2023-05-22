from printing import *
def sort_list_of_objects(data, sort_param='title', reverse=False):
    sorted_data = sorted(data, key=lambda x: (getattr(x, sort_param), '') if getattr(x, sort_param) is not None else ('', ''), reverse=reverse)

    return sorted_data



