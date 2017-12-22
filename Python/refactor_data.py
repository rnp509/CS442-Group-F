import csv

data = {}

with open("data/data.csv") as csvfile:
  reader = csv.DictReader(csvfile)
  for index, row in enumerate(reader):
    currency = row['Country']
    if not data.get(currency):
      data[currency] = []
    data[currency].append({
      'day': row['Day'],
      'open': row['Open'],
      'high': row['High'],
      'low': row['Low'],
      'close': row['Close'],
      'volume': row['Volume'],
      'market_cap': row['Market Cap']
    })

#for index, item in enumerate(data):
#  try:
#    data[index]['previous_day_open'] = data[index + 1]['open']
#  except:
#    pass

for currency in data:
  with open("data/" + currency + ".csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile, [
      'day',
      'open',
      'high',
      'low',
      'close',
      'volume',
      'market_cap'
    ])
    writer.writeheader()
    for row in data[currency]:
      writer.writerow(row)

