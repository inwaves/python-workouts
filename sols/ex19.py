def passwd_to_dict(filepath) -> dict:
    user_details = {}
    with open(filepath) as fileobj:
        for line in fileobj:
            if any([line.startswith(("#", "_", "\n")), ":" not in line]):
                continue
            elems = line.split(":")
            user_details[elems[0].strip()] = int(elems[2].strip())
    return user_details
