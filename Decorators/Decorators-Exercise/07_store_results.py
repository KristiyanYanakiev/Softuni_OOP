class store_results:

    _DIR_NAME = "files"
    _FILE_NAME = "log.txt"
    PATH = f"{_DIR_NAME}/{_FILE_NAME}"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        text_to_add =(f"Function '{self.func.__name__}' was called. Result: {self.func(*args, **kwargs)}\n")

        with open(self.PATH, "a") as log_file:
            log_file.write(text_to_add)




@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)