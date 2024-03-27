import os, requests
import pandas as pd
from datetime import datetime, timedelta
#place = pd.read_csv("location.csv")
#locations = [(32.929, -95.770), (5, 10)]

def down(dzz,csv,sdate,edate):
    sssdate = datetime.strptime(sdate, "%d/%m/%Y")
    ssdate = sssdate.strftime("%Y%m%d")
    eedate=(datetime.strptime(edate, "%d/%m/%Y")).strftime("%Y%m%d")
    
    base_url = r"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=T2M_MAX,T2M_MIN,ALLSKY_SFC_SW_DWN,PRECTOTCORR&community=AG&longitude={longitude}&latitude={latitude}&start={sdate}&end={edate}&format=CSV"
    previous_dis = None
    #current_directory = current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #folder_name = "in"
    # Construct the path to the "in" folder using os.path.join
    output = dzz
    #output = os.path.join(current_directory, folder_name)
    
    place = pd.read_csv(csv)
    for index, row in place.iterrows():
        # Get latitude and longitude from the CSV
        latitude = row["Latitude"]
        longitude = row["Longitude"]
        dis = row["Location_Name"].upper()
        api_request_url = base_url.format(longitude=longitude, latitude=latitude, sdate=ssdate, edate=eedate)
        response = requests.get(url=api_request_url, verify=True, timeout=30.00)
        print(response)
        print(api_request_url)
        
        if dis != previous_dis:
            inde = 1
        fsn = str(inde).zfill(2)
        previous_dis = dis
        inde += 1
    
        if response.status_code == 200:
            filename = f"{dis[:3]}{fsn}.csv"
            filepath = os.path.join(output, filename)
            
            # Save the CSV data to a file
            with open(filepath, 'wb') as file_object:
                file_object.write(response.content)
            df = pd.read_csv(filepath, skiprows=range(0, 14))
            #print(df)
            df = df.iloc[:, 2:]
            df.columns = ['TMAX','TMIN','SRAD','RAIN']
            start_date = ssdate
            end_date = eedate
            date_range = pd.date_range(start_date, end_date, periods=len(df))
            df.insert(0, 'DATE', date_range.strftime('%Y/%m/%d'))
            #print(df[240:])
            df.to_csv(filepath, index=False)
        else:
            print(f"Failed to retrieve data for latitude {latitude} and longitude {longitude}. Status code: {response.status_code}")
    
