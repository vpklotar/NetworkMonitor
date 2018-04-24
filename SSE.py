"""Substition Engine"""
substitution_dict = {}

def substitue(value, custom_dict = {}):
    """Will replace all match $SUBSTITION$ with there corresponding values"""
    re_val = value
    for match, replacement in custom_dict.items():
        re_val = re_val.replace("$%s$" % match, replacement)
    for match, replacement in substitution_dict.items():
        re_val = re_val.replace("$%s$" % match, replacement)
    return re_val

def register_substitiution(key, value):
    """Register a subtitiution that will be applied when a substitution is requested"""
    substitution_dict[key] = value