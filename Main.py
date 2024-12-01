print("*****This Is a project based on timezone converter which is made by********")
print("| VISHNU VARDHAN.N | LAKSHMI NARAYANA.N | C.CHARAN KUMAR REDDY |")



#import python_library#
import pytz
import datetime

#taking input from the user#
print("enter YYYY MM DD in this format:")
year,month,day = map(int,input().split())
print("Enter Time in HH MM In this format")
hour,minute = map(int,input().split())


users_time=datetime.datetime(year,month,day,hour,minute)
print(users_time.isoformat())
print("Enter the preferred country:")
country = input()

if "india" in country:
   india_timezone = pytz.timezone('Asia/Kolkata')
   india_time = pytz.utc.localize(users_time).astimezone(india_timezone)
   print("Time in INDIA is:", india_time.isoformat())

elif "usa" in country or "america" in country:
    eastern_timezone = pytz.timezone('America/New_York')
    eastern_time = pytz.utc.localize(users_time).astimezone(eastern_timezone)
    print("Time in USA is:", eastern_time.isoformat())
    
elif "uk" in country or "britain" in country:
    now_uk = pytz.timezone('Europe/London')
    now_uk = pytz.utc.localize(users_time).astimezone(now_uk)
    print("Time in UK is:", now_uk.isoformat())    

elif "china" in country or "hong kong" in country:
    china_timezone = pytz.timezone('Asia/Shanghai')
    china_time = pytz.utc.localize(users_time).astimezone(china_timezone)
    print("Time in CHINA is:", china_time.isoformat())

elif "japan" in country or "tokyo" in country:
    japan_timezone = pytz.timezone('Asia/Tokyo')
    japan_time = pytz.utc.localize(users_time).astimezone(japan_timezone)
    print("Time in JAPAN is:", japan_time.isoformat())

elif "canada" in country or "mexico" in country:
    toronto_timezone = pytz.timezone('Canada/newfoundland')
    toronto_time = pytz.utc.localize(users_time).astimezone(toronto_timezone)
    print("Time in CANADA is:", toronto_time.isoformat())

elif "russia" in country or "moscow" in country:
    moscow_timezone = pytz.timezone('Europe/Moscow')
    moscow_time = pytz.utc.localize(users_time).astimezone(moscow_timezone)
    print("Time in RUSSIA is:",moscow_time.isoformat())

elif "germany" in country or "berlin" in country:
    timezone = pytz.timezone('Europe/Berlin')
    time = pytz.utc.localize(users_time).astimezone(timezone)
    print("Time in Germany is:",time.isoformat())
    
elif "france" in country or "paris" in country:
    paris_timezone = pytz.timezone('Europe/Paris')
    paris_time = pytz.utc.localize(users_time).astimezone(paris_timezone)
    print("Time in FRANCE is:",paris_time.isoformat())

elif "saudi arabia" in country or "dubai" in country:
   saudi_timezone = pytz.timezone('Asia/Riyadh')
   saudi_time = pytz.utc.localize(users_time).astimezone(saudi_timezone)
   print("Time in SAUDI ARABIA is:",saudi_time.isoformat())
   
elif "italy" in country or "rome" in country:
    italy_timezone = pytz.timezone('Europe/Rome')
    italy_time = pytz.utc.localize(users_time).astimezone(italy_timezone)
    print("Time in ITALY is:",italy_time.isoformat())
    
elif "srilanka" in country or "colombo" in country:
    sri_lanka_timezone = pytz.timezone('Asia/Colombo')
    sri_lanka_time = pytz.utc.localize(users_time).astimezone(sri_lanka_timezone)
    print("Time in SRI LANKA is:",sri_lanka_time.isoformat())
    
else:
    print("The specified country/timezone is not supported in this program.")
    