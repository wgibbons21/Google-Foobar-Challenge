def answer(x, y, z):
    dates = [x, y, z]
    dates.sort()

    if x == y and y == z:   #Special case x=y=z
        month = dates[1]
        day =   dates[1]
        year =  dates[1]
        return str(month).zfill(2)+"/"+str(day).zfill(2)+"/"+str(year).zfill(2)


    if dates[2] > 31:
        year = dates[2]
        if dates[1] > 12 and dates[1] < 32:
            month = dates[0]
            day = dates[1]
            return str(month).zfill(2)+"/"+str(day).zfill(2)+"/"+str(year).zfill(2)
        elif dates[1] == dates[0] and dates[1] < 13:
            month = dates[0]
            day = dates[1]
            return str(month).zfill(2)+"/"+str(day).zfill(2)+"/"+str(year).zfill(2)
        else:
            return "Ambiguous"
    else:   #year is <= 31
        if dates[0] == 2:   #case of Feb
            if dates[1] == 28 and (dates[2] == 29 or dates[2] == 30 or dates[2] == 31):
                year = dates[2]
                month = dates[0]
                day = dates[1]
                return str(month).zfill(2)+"/"+str(day).zfill(2)+"/"+str(year).zfill(2)
            else:
                return "Ambiguous"
        elif dates[0] in [4, 6, 9, 11]: #case of 30 day months
            if dates[1]==30 and dates[2]==31:
                year = dates[2]
                month = dates[0]
                day = dates[1]
                return str(month).zfill(2)+"/"+str(day).zfill(2)+"/"+str(year).zfill(2)

        elif (dates[2] == dates[1]) and (dates[1] > 12):
            year = dates[2]
            month = dates[0]
            day = dates[1]
            return str(month).zfill(2)+"/"+str(day).zfill(2)+"/"+str(year).zfill(2)
        elif dates[0] == dates[1] and dates[1] <= 12 and dates[2] > 12:
            year = dates[2]
            month = dates[0]
            day = dates[1]
            return str(month).zfill(2)+"/"+str(day).zfill(2)+"/"+str(year).zfill(2)
        elif dates[0] <= 12 and dates[1] > 12 and dates[2] > 12 and dates[2] ==dates[1]:
            month = dates[0]
            day = dates[1]
            year = dates[2]
            return str(month).zfill(2)+"/"+str(day).zfill(2)+"/"+str(year).zfill(2)
        else:
            return "Ambiguous"


a = 2
b = 12
c = 31

print answer(a,b,c)

