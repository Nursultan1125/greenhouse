from database.sqlite3con import DBHelper
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

db = DBHelper()

data_date_time = db.select_pipe_cols(1, 'date_time')
temper = db.select_pipe_cols(1, 'temp2')
dt = []
for date_time in data_date_time:
    tmp = datetime.datetime.strptime(date_time[0], "%Y-%m-%d %H:%M:%S")
    dt.append(tmp)

print(temper)
print(dt)

fig, ax = plt.subplots()
ax.plot_date(dt, temper, '-o')

ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
fig.autofmt_xdate()

plt.show()



