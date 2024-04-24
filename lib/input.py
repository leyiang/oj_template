# alias print so converter will convert to return stmt
rprint = print

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
