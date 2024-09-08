while True:
    print("this is the first pythob file on debian system. press 123 to exit...")
    press = input("")
    if press == "123":
        exit()
    elif press == "numpy":
        import numpy
        print("numpy pip imported where version: %s"%numpy.__version__)