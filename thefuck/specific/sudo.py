from decorator import decorator


@decorator
def sudo_support(fn, command):
    """Removes sudo before calling fn and adds it after."""
    if not command.script.startswith('sudo '):
        return fn(command)

    result = fn(command.update(script=command.script[5:]))

    if result and isinstance(result, str):
        return 'sudo {}'.format(result)
    elif isinstance(result, list):
        return ['sudo {}'.format(x) for x in result]
    else:
        return result
