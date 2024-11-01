from copy import deepcopy


def get_keys_values(d, current_path=""):
      """Gets all keys and values from a nested dictionary."""

      for key, value in d.items():
          key_path = f"{current_path}.{key}" if current_path else key

          if isinstance(value, dict):
              # Recursive call for nested dictionaries
              yield from get_keys_values(value, key_path)
          else:
              # Yield key-value pair for non-dictionary values
              yield key_path, value




def validate(data, template):
    """Validates the structure of a nested dictionary against a template."""

    template_tuple=[]
    template_key=[]
    template_value=[]
    data_tuple=[]
    data_key=[]
    data_value=[]
    # Get all keys and values
    for key_path, value in get_keys_values(template):
        template_key.append(key_path)
        template_value.append(value)
        template_tuple.append((key_path,value))

    # Get all keys and values
    for key_path, value in get_keys_values(data):
        data_key.append(key_path)
        data_value.append(type(value))
        data_tuple.append((key_path,type(value)))

    Missing_key_value=set(template_tuple).difference(data_tuple)
    Extra_key_value=set(data_tuple).difference(template_tuple)
    first_missing_key = [element[0] for element in Missing_key_value]
    first_extra_key = [element[0] for element in Extra_key_value]
    first_missing_value = [element[1] for element in Missing_key_value]
    first_extra_value = [element[1] for element in Extra_key_value]
    empty_key_value = set(template_key).intersection(data_key) 



    if tuple(Missing_key_value)==set() :
        return True, ''
    elif tuple(Extra_key_value)==set() :
        return True, ''
    elif empty_key_value==set() :
        return False, f"mismatched keys: {template_key[0]}"
    elif (first_missing_key==first_extra_key) & (first_missing_value!=first_extra_value):
        return False, f"bad type: {first_missing_key[0]}"
    elif tuple(Missing_key_value):
        return False, f"mismatched keys: {tuple(Missing_key_value)[0][0]}"
    elif tuple(Extra_key_value):
        return False, f"mismatched keys: {tuple(Extra_key_value)[0][0]}"

    else:
      return True, ''

