#!/usr/bin/env python3

import sys
import csv
from datetime import datetime, timedelta
import math

def find_pattern(filename, currency_name, weight=1.15, window=31):
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
  for item in currencies[currency_name]:
    eth_market_cap[item['day']] = item['market_cap']

  pattern_days = {}
  currencies_to_analyze = ["bitcoin", "dogecoin", "ethereum", "omisego", "ripple"]

  for currency, days in currencies.items():
    if currency not in currencies_to_analyze:
      continue
    window_size = window
    half_window_size = math.floor((window_size - 1) / 2)
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
        (middle_day_close > weight * left_avg and middle_day_close > weight * right_avg) or
        (middle_day_close < left_avg / weight and middle_day_close < right_avg / weight)
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
  return dates, text, market_cap

if __name__ == "__main__":
  if len(sys.argv) < 3:
    print("Usage: " + sys.argv[0] + " <csv file> <name of currency to annotate> <optional: deviation in average considered significant, default=1.15> <optional: window size in days, default=31>")
  else:
    if len(sys.argv) == 3:
      dates, text, market_cap = find_pattern(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
      dates, text, market_cap = find_pattern(sys.argv[1], sys.argv[2], float(sys.argv[3]))
    else:
      dates, text, market_cap = find_pattern(sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4]))
    print(dates)
    print(text)
    print(market_cap)
