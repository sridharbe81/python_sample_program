try:                                       # try block will execute the statement inside the block
    with open('CEC_COPY.txt') as rf:
        rf.read()
    # name = vivek
    # raise NameError                      # we can manually raise the exception
except FileNotFoundError as e:
    print(e)
except NameError as e:
    print(e)
else:                                    # else part will run if we are not having any exception, it will not run if exception was caught
    print('hi')
finally:                                 # Finally will execute no matter what
    print('Executing Finally')


