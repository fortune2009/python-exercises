put = int(input("Enter seconds within range 1 - 86400 to find current time: "))

mins = put/60%60
sec = put%60
hrs = put/60/60

print(int(hrs), " Hours, ", int(mins)," Minutes, ", sec, " Seconds.")  

