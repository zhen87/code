import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
  #将用户输入的时间转换为datetime
  tz = re.match(r'^(UTC)([\+|-]\d+)\:00$', tz_str)
  dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
  tz_utc = timezone(timedelta(hours=int(tz.group(2))))
  tz_dt = dt.replace(tzinfo=tz_utc)
  utc_dt = tz_dt.astimezone(timezone(timedelta(hours=0)))
  return utc_dt.timestamp()
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')