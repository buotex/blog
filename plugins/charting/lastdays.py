import datetime
import os

with open('daily.json','w') as fg:

    tuples = []
    with open('daily.txt') as filehandle:
        for line in filehandle:
            splitup = line.split(" ")
            date = splitup[0]
            added = splitup[4]
            removed = splitup[6]
            netadded = int(added) - int(removed)
            tuples.append((date, netadded))

    fg.write('{\n"cols":[{"id":"Col1","label":"","type":"date"},\
    {"id":"Col1","label":"","type":"number"}],\n')
    fg.write('"rows": [')
    for date, num in tuples:
        #t = datetime.datetime.fromtimestamp(stamp)
        timetuple = [int(x) for x in date.split("-")]
        print timetuple
        datestring = '"Date(%d, %d, %d)","f": "%d-%d-%d"' %(timetuple[0], timetuple[1]-1, timetuple[2],
                                                                       timetuple[0], timetuple[1]-1, timetuple[2])
        print datestring
        fg.write('{"c":[{"v":%s},{"v":%d}]},\n' % (datestring, num))

    fg.seek(-2, os.SEEK_END)
    fg.truncate()
    fg.write(']}')
    fg.close()
