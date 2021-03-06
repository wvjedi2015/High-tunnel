#!/usr/bin/python
import pygal 
import csv

## Parse log
with open('log.csv', 'rb') as csvfile:
    read = csv.reader(csvfile)
    for row in read:
         currentHumidity = row[5]

gauge_chart = pygal.Gauge(show_legend=False,human_readable=True,style=pygal.style.styles['default'](label_font_size=24))
gauge_chart.range = [30, 100]
gauge_chart.add('', currentHumidity)
gauge_chart.render_to_file('/var/www/html/humid_gauge.svg') 
print currentHumidity
