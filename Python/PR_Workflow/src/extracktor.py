
def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, val_ue in obj.items():
                if isinstance(val_ue, (dict, list)):
                    extract(val_ue, arr, key)
                elif k == key:
                    arr.append(val_ue)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values
