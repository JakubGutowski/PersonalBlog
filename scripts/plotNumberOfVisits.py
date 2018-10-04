import os, sqlite3

import matplotlib.pyplot as plt

from datetime import datetime
from calendar import monthrange

# Read date and number of days in this month
todayDate = datetime.now()
thisMonth = todayDate.month
daysInThisMonth = monthrange(todayDate.year, todayDate.month)[1]

# Connect to DB and select records
dbTargetPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'test', 'db.sqlite3'))
conn = sqlite3.connect(dbTargetPath, detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
cursor.execute("SELECT pub_date FROM blog_visitorip ;")

# Create list of visits in this month
visitsList = []
[visitsList.append(item[0]) for item in cursor.fetchall()]
visitsList = [datetime.strptime(x, '%Y-%m-%d %H:%M:%S.%f') for x in visitsList]
visitsThisMonth = list(filter(lambda x: x.month == thisMonth, visitsList))
countVisitsInDay = []
for day in range(1, daysInThisMonth):
    countVisitsInDay.append(int(len(list(filter(lambda x: x.day == day, visitsThisMonth)))))

barChartFilePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'test',
                                                'visitsChart' + datetime.strftime(todayDate, '%m%Y')))
# Create create barchart of number of visits each day
plt.bar(range(1, daysInThisMonth), countVisitsInDay, 0.9, color='teal')
plt.yticks(range(1, max(countVisitsInDay) + 2))
plt.legend(['Number of visits'])
plt.title('Site visits in month:' + datetime.strftime(todayDate, '%B %Y'))
plt.savefig(barChartFilePath, transparent=True)
plt.show()
