import csv
from datetime import datetime, timedelta

currencies = {}

with open("data.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  for index, row in enumerate(reader):
    currencies.setdefault(row['Country'], list()).append({
      'day': row['Day'],
      'open': row['Open'],
      'high': row['High'],
      'low': row['Low'],
      'close': row['Close'],
      'volume': row['Volume'],
      'market_cap': row['Market Cap']
    })

eth_market_cap = {}
for item in currencies["ethereum"]:
  eth_market_cap[item['day']] = item['market_cap']

pattern_days = {}
currencies_to_analyze = ["bitcoin", "dogecoin", "ethereum", "omisego", "ripple"]

for currency, days in currencies.items():
  if currency not in currencies_to_analyze:
    continue
  window_size = 31
  half_window_size = int((window_size - 1) / 2)
  for i in range(0, len(days)):
    if i - window_size < 0 or i + window_size >= len(days):
      continue
    left_total = 0.
    right_total = 0.
    for j in range(0, half_window_size):
      left_total += float(days[i + j]['close'])
      right_total += float(days[i + window_size - 1 - j]['close'])
    left_avg = left_total / half_window_size
    right_avg = right_total / half_window_size
    middle_day = days[i + half_window_size]
    middle_day_close = float(middle_day['close'])
    if (
      (middle_day_close > 1.15*left_avg and middle_day_close > 1.15*right_avg) or
      (middle_day_close < left_avg/1.15 and middle_day_close < right_avg/1.15)
    ):
      pattern_days.setdefault(currency, list()).append(middle_day['day'])

rev_multidict = {}
for currency, days in pattern_days.items():
  for day in days:
    rev_multidict.setdefault(day, set()).add(currency)

dates = []
text = []
market_cap = []
for key, currencies in rev_multidict.items():
  if len(currencies) > 1:
    date = datetime.strptime(key, "%Y%m%d")
    start = date - timedelta(days=7)
    end = date - timedelta(days=1)
#    print(date.strftime("%m/%d/%Y") + " : " + ", ".join(values) + " : https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:" + start.strftime("%m/%d/%Y") + ",cd_max:" + end.strftime("%m/%d/%Y"))
    if eth_market_cap.get(key):
      dates.append(key)
      text.append("https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:" + start.strftime("%m/%d/%Y") + ",cd_max:" + end.strftime("%m/%d/%Y"))
      market_cap.append(eth_market_cap[key])
print(dates)
print(text)
print(market_cap)
