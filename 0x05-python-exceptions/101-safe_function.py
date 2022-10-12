#!/usr/bin/python3
def safe_function(fct, *args):
    import sys as s
    try:
        ret = fct(*args)
        return ret
    except Exception as e:
        print("Exception: {}".format(e), file=s.stderr)
        return None
