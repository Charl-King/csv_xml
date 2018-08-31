import pandas as pd
import datetime
import ctypes; lib = ctypes.WinDLL('msvcp90.dll')
MONTH = 1
YEAR = 2010

#YEAR = raw_input("Enter year: ")
#type(YEAR)
#MONTH = raw_input("Enter month: ")
#type(MONTH)
def convert_row(row):

    date = datetime.datetime.strptime(row.DateTime, "%m/%d/%Y  %H:%M:%S").strftime("%m-%d-%Y")
    dti = datetime.datetime.strptime(row.DateTime, "%m/%d/%Y  %H:%M:%S")
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

    impact = {  0:"Low", 1:"Medium", 2:"High", 3:"VeryHigh"}
    imp = impact.get(row.Volatility,)
    if (dti.month == int(MONTH)):
        return """<event>
        <title>%s</title>
        <country>%s</country>
        <date><![CDATA[%s]]></date>
        <time><![CDATA[%s]></time>
        <impact><![CDATA[%s]></impact>
        <forecast><![CDATA[%s]></forecast>
        <previous><![CDATA[%s]></previous>
        </event>\n""" % (row.Name, cur, date, time, imp, row.Actual, row.Previous)
    else:
        return ""
    
while (YEAR <= 2020):
    while (MONTH <= 12):
        source_file = str(YEAR) + ".csv"
        df = pd.read_csv(source_file, sep=',')
        file_name = "FF_iNews" + str(YEAR) + str(MONTH) + ".xml"
        file = open (file_name, "w")
        file.write(''.join(df.apply(convert_row, axis=1)))
        MONTH = MONTH + 1
    MONTH = 1
    YEAR = YEAR + 1
