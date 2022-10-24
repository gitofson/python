import calendar, datetime, time

dc = datetime.datetime(2015, 10, 25, 14, 32, 10)
# cal = calendar.timegm(dc.utctimetuple())
print(time.strftime("%Y - %m - %d %H : %M : %S", dc.utctimetuple()))
# ziskani dnesniho data
now = time.asctime()
#print(time.strftime("%Y - %m - %d %H : %M : %S", datetime.datetime().now()))
print(now)