# CS 442 Group F

## Overview

This project allows a user to find points of interest across multiple timeseries datasets by detecting simultaneous deviations in a weighted window average. This can be used to automatically annotate the timeseries with relevant news articles, essentially providing a summary of events that have occured.

We apply this to cryptocurrency data to depict how changes in the price of Bitcoin has a large impact on the pricing of other cryptocurrencies. We assume this is due to the Proof-of-Concept nature of Bitcoin and people use its success as a paradigm for pricing cryptocurrencies in general.

## Requirements

We are currently using Python 3.5.

## Usage

```
./find_pattern.py <csv file> <name of currency to annotate> <optional: deviation in average considered significant, default=1.15> <optional: window size in days, default=31>
```

## Output

Annotation data (date, top news articles, market cap of currency) that can be fed into a visualization framework like plot.ly.

E.g.,
```
./find_pattern.py data.csv ethereum
```

```
['20160802', '20170831', '20170715', '20170716', '20170402', '20170901', '20170523', '20170830', '20160619', '20170914']
['https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:07/26/2016,cd_max:08/01/2016', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:08/24/2017,cd_max:08/30/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:07/08/2017,cd_max:07/14/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:07/09/2017,cd_max:07/15/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:03/26/2017,cd_max:04/01/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:08/25/2017,cd_max:08/31/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:05/16/2017,cd_max:05/22/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:08/23/2017,cd_max:08/29/2017', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:06/12/2016,cd_max:06/18/2016', 'https://www.google.com/search?q=bitcoin+site:wsj.com&tbs=cdr:1,cd_min:09/07/2017,cd_max:09/13/2017']
['903,978,000', '35,701,500,000', '18,630,200,000', '15,823,100,000', '4,582,700,000', '36,182,900,000', '15,688,000,000', '34,848,400,000', '906,292,000', '26,166,100,000']
```
