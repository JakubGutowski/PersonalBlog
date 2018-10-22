import os, sqlite3

import matplotlib.pyplot as plt

from datetime import datetime
from calendar import monthrange


class VisitModel():
    def __init__(self, model):
        self.pub_date = datetime.strptime(model[0], '%Y-%m-%d %H:%M:%S.%f')
        self.ip_address = model[1]

# Read date and number of days in this month
todayDate = datetime.now()
thisMonth = todayDate.month
daysInThisMonth = monthrange(todayDate.year, todayDate.month)[1]

# Connect to DB and select records
dbTargetPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'db.sqlite3'))
conn = sqlite3.connect(dbTargetPath, detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
cursor.execute("SELECT pub_date, ip_address FROM blog_visitorip ;")

# Create list of visits in this month
visitsList = []
[visitsList.append(VisitModel(item)) for item in cursor.fetchall()]
visitsThisMonth = list(filter(lambda x: x.pub_date.month == thisMonth, visitsList))

visitsInDay = []
countVisitsInDay = []
countUniqueVisitsInDay = []
for day in range(1, daysInThisMonth):
    ipVisitsInDay = []
    visitsInDay.append(list(filter(lambda x: x.pub_date.day == day, visitsThisMonth)))
    countVisitsInDay.append(len(visitsInDay[day - 1]))
    [ipVisitsInDay.append(x.ip_address) for x in visitsInDay[day - 1]]
    countUniqueVisitsInDay.append(len(set(ipVisitsInDay)))
    print(countUniqueVisitsInDay)
barChartFilePath = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'source', 'blog', 'static', 'visitStatistics',
                 'visitsChart' + datetime.strftime(todayDate, '%m%Y')))

# Create create barchart of number of visits each day
plt.bar(range(1, daysInThisMonth), countVisitsInDay, 0.9, color='#D3D3D3')
plt.bar(range(1, daysInThisMonth), countUniqueVisitsInDay, 0.9, color='teal')
plt.yticks(range(1, max(countVisitsInDay) + 2, 5))
plt.legend(['Number of visits', 'Number of unique visits'])
plt.title('Site visits in month:' + datetime.strftime(todayDate, '%B %Y'))
plt.savefig(barChartFilePath, transparent=True)
plt.show()
