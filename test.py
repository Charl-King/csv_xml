import pandas as pd
import datetime

def convert_row(row):
    date = datetime.datetime.strptime(row.DateTime, "%m/%d/%Y  %H:%M:%S").strftime("%m-%d-%Y")
    time = datetime.datetime.strptime(row.DateTime, "%m/%d/%Y  %H:%M:%S").strftime("%#I:%M %p")

    countries = {   "Australia" : "AUD",
                    "Canada"    : "CAD",
                    "China"     : "CNY",
                    "European Monetary Union" :	"EUR",
                    "France"    : "EUR",
                    "Germany"   : "EUR",
                    "Italy"     : "EUR",
                    "Japan"     : "JPY",
                    "New Zealand": "NZD",
                    "Spain"     : "EUR",
                    "Switzerland" : "CHF",
                    "United Kingdom" : "GBP",
                    "United States"  : "USD"}
    cur = countries.get(row.Country,)

    impact = {  0:"Low", 1:"Medium", 2:"High"}
    imp = impact.get(row.Volatility,)

    return """<event>
    <title>%s</title>
    <country>%s</country>
    <date><![CDATA[%s]]></date>
    <time><![CDATA[%s]></time>
    <impact><![CDATA[%s]></impact>
    <forecast><![CDATA[%s]></forecast>
    <previous><![CDATA[%s]></previous>
</event>""" % (
    row.Name, cur, date, time, imp, row.Actual, row.Previous)
    
df = pd.read_csv('2010.csv', sep=',')

file = open ("test.xml", "w")
file.write('\n'.join(df.apply(convert_row, axis=1)))
