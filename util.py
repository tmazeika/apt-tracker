def printCsvLine(*args):
    quoted = ['"' + str(arg).replace('"', '""') + '"' for arg in args]
    print(','.join(quoted))