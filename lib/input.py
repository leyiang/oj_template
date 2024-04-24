INTL = "int_list"

def getIntList():
    raw = input().strip(" []")
    return list(map(int, raw.split(",")))

def inputLoop(callback, inputInfo):
    while True:
        try:
            data = []
            for inputType in inputInfo:
                if inputType == INTL:
                    data.append( getIntList() )
            callback(*data)
        except EOFError:
            break

# will be convert to return statement
def rprint(*args, **kwargs):
    print(*args, **kwargs)
