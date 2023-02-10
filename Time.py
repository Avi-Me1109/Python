time = int(input("Enter number of seconds: "))
convertedTime = 0.0
changingTime = time

if (time >= 60 and time < 3600):
    minutes = time // 60
    time %= 60
    seconds = time

    print(minutes, " minutes ", seconds, " seconds")

if(time >= 3600 and time < 86400):
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    print(hour, " hours", minutes, " minutes ", seconds, " seconds")

if(time >= 86400):
    day = time // (24 * 3600)
    time = time % (24 * 3600)   
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time

    print(day, " days", hour, " hours", minutes, " minutes ", seconds, " seconds")

