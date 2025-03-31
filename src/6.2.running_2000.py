import time


def running_2000(f, *args, **kwargs):

    """
    The func calculate the time that take to func to run on paramters

    params: function and and parametes
    return: the time that take to func to run  on this parameters
    """
    start_time = time.perf_counter()
    result = f(*args, **kwargs)
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    return elapsed_time



if __name__ == "__main__":
    print(running_2000(print, "Hello"))
    print(running_2000(zip, [1, 2, 3], [4, 5, 6]))
    print(running_2000("Hi {name}".format, name="Bug"))
