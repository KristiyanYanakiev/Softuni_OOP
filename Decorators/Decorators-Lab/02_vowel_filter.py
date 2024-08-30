def vowel_filter(func):
    def wrapper(*args, **kwargs):
        return [l for l in func(*args, **kwargs) if l.lower() in "aeiuyo"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())