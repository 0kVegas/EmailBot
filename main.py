import FunctionFile

if __name__ == '__main__':
    wait = 32
    while True:
        # Send emails
        if FunctionFile.CheckTime(FunctionFile.getTime()):
            size = len(list(FunctionFile.OpenList()))
            if size > 1:
                items = FunctionFile.OpenList()
                email = FunctionFile.Email(FunctionFile.Receiver())

                if int(wait) == int(FunctionFile.getTime()[1]):
                    email.send()
                    FunctionFile.AppendItem()
                    FunctionFile.PopItem(items)
                    wait = FunctionFile.Pause()
                    print(wait)
                    print(FunctionFile.getTime()[1])
