def whitelist():
    def decorator(function):
        return function

    return decorator


def has_permission(doctype, ptype):
    return True


def throw(message):
    raise Exception(message)