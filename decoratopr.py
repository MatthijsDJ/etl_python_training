def max(value):
    def max_result(old_function):
        def new_function(first, second):
            result = old_function(first, second)
            if result > value:
                result = value
            return result
        return new_function
    return max_result


@max(100)
def add(first, second):
    return first + second