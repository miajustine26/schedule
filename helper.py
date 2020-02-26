from datetime import datetime

def time():
    day=int(datetime.now().weekday())
    dayList= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dayOfTheWeek=dayList[day]
    hour=datetime.now().hour
    mins=datetime.now().minute
    #find the current period
    if hour < 8:
        period="none"
    elif hour <= 9 and mins <= 15:
        period="first"
    elif hour <= 10:
        period="second"
    elif hour <= 10 and mins <= 45:
        period="third"
    elif hour <= 10 and mins <= 55:
        period="snack"
    elif hour <= 11 and mins <= 40:
        period="fourth"
    elif hour <= 12 and mins <= 25:
        period="fifth"
    elif hour <= 1 and mins <= 10:
        period="lunch"
    elif hour <= 1 and mins <= 55:
        period="sixth"
    elif hour <= 2 and mins <= 40:
        period="seventh"
    elif hour <= 3 and mins <= 25:
        period="eighth"

    timeData= {
        "day": dayOfTheWeek,
        "hour": hour,
        "minute": mins,
        "period": period
    }
    return timeData
