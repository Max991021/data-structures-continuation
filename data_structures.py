def split_coords(coordinates):
    return tuple(list(i) for i in zip(*coordinates))
print(split_coords([(12, 45), (15, 48), (18, 51)]))

def flatten_list(nested_list):
    new = []
    for item in nested_list:
        if isinstance(item,list):
            new.extend(flatten_list(item))
        else:
            new.append(item)
    return new

def create_id_lookup(user_data):
    return {name: number for number,name in enumerate(user_data)}

def top_performer(student_data):
    return max(student_data,key=student_data.get)

def sort_by_length(names):
    return sorted(names,key=len)

def group_by_category(items):
    new = {}
    
    for item in items:
        name = item['name']
        ty = item['type']
        new.setdefault(ty,[]).append(name)
    return new

def sort_dict_by_value(data):
    return {item:data[item] for item in sorted(data, key =data.get)}

def rotate_list(nums, k):
    if len(nums)<k:
        k = k-len(nums)
    return nums[-k:]+nums[:-k]
print(rotate_list([1, 2], 3))

def sort_emails_by_domain(emails):
    return ''

def is_subset(list_a, list_b):
    return True if set(list_a).issubset(set(list_b)) else False
print(is_subset([1, 2], [1, 2, 3, 4]))

def remove_dictionary_key(data, keys_to_remove):
    return ''

def invert_dictionary(data):
    return ''

def recursive_sum(n):
    return ''

def fibonacci_generator(n):
    return ''