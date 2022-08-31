import FunctionFile

if __name__ == '__main__':
    print("Up and Running")
    minute = 2  # wait time is not set to 0 it means message will be sent at 0th minute of the hour
    sentToDB = FunctionFile.Database("SentTo.DB")
    # sentToDB.Setup()
    sentToDB.SearchGeneral()

    while True:
        # Send emails
        #if FunctionFile.CheckTime(FunctionFile.getTime()):
            size = len(list(FunctionFile.OpenList('EmailTextFile.txt')))
            if size > 1:
                items = FunctionFile.OpenList('EmailTextFile.txt')
                email = FunctionFile.Email(FunctionFile.Receiver())

                if int(minute) == int(FunctionFile.getTime()[1]):
                    #email.send()
                    sentToDB.AddInfo(FunctionFile.emailSetUp())
                    FunctionFile.PopItem(items)
                    wait = FunctionFile.Pause()

        # Add Emails to file
        #if FunctionFile.getTime()[1] == 0:  # Hourly Check
            #FunctionFile.uploadEmails()

        #elif FunctionFile.getTime()[1] == 50 and FunctionFile.getTime()[2] < 5:  # Warning for email uploads
            #print('Emails Will be uploaded in 10 minutes')
