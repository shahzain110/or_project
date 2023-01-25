import base64
from fastapi import FastAPI, File, UploadFile, Form, Header, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import os 
import numpy as np
import pandas as pd
from app import Exponential_distribution
from app import Normal_distribution
from app import Uniform_Distribution
from fastapi.middleware.cors import CORSMiddleware
import dataframe_image as dfi

#Fast API Object
app = FastAPI() 

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )


@app.post('/Uniform_distribution')
async def Uniform(timer: int = Form(...), records: int = Form(...)):
    try:
        
        s=Uniform_Distribution.Bank_Simulation()

        df=pd.DataFrame(columns=['Average interarrival time','Average service time teller1','Average service time teller 2','Utilization teller 1','Utilization teller 2',\
            'People who had to wait in line','Total average wait time','Lost Customers'])
        
        for i in range(int(records)):
            np.random.seed(i)
            
            while s.clock <= int(timer):
                s.time_adv() 
            a=pd.Series([s.clock/s.num_arrivals,s.dep_sum1/s.num_of_departures1,s.dep_sum2/s.num_of_departures2,s.dep_sum1/s.clock,\
                        s.dep_sum2/s.clock,s.number_in_queue,s.total_wait_time,s.lost_customers],index=df.columns)
            df=df.append(a,ignore_index=True)   

            
        dfi.export(df, 'uniform.png')
        with open("uniform.png", "rb") as img_file:
            my_string = base64.b64encode(img_file.read())

        avg_teller_1 = df["Utilization teller 1"].mean()
        avg_teller_2 = df["Utilization teller 2"].mean()
        number_people = df["People who had to wait in line"].sum()
        avg_wait = df["Total average wait time"].mean()
        avg_lost = df["Lost Customers"].mean()


        thisdict = {
        "UTILIZATION OF TELLER 1 : ": avg_teller_1*100,
        "UTILIZATION OF TELLER 2 : ": avg_teller_2*100,
        "NUMBER OF PEOPLE WHO HAD TO WAIT : " : number_people,
        "AVERAGE WAIT TIME PER CUSTOMER : " : avg_wait*100,
        "AVERAGE LOST CUSTOMERS : " : avg_lost*100 }

        result = pd.DataFrame.from_dict(thisdict, orient = 'index')
        dfi.export(result, 'RESULTS.png')

        print("************* RESULTS **************")
        print("UTILIZATION OF TELLER 1 : ",avg_teller_1*100)
        print("UTILIZATION OF TELLER 2 : ",avg_teller_2*100)
        print("NUMBER OF PEOPLE WHO HAD TO WAIT : ",number_people)
        print("AVERAGE WAIT TIME PER CUSTOMER : ",avg_wait*100)
        print("AVERAGE LOST CUSTOMERS : ",avg_lost*100)

        return my_string
    except Exception as e:
        print(e)
        print("Exception in Uniform Distribution")
        return {"Message": "Exception"}


@app.post('/Exponential_distribution') 
async def Exponential(timer: int = Form(...), records: int = Form(...)):
    try:
        s= Exponential_distribution.Bank_Simulation()
        df=pd.DataFrame(columns=['Average interarrival time','Average service time teller1','Average service time teller 2','Utilization teller 1','Utilization teller 2',\
            'People who had to wait in line','Total average wait time','Lost Customers'])

        # timer = input("Enter Duration : ")
        # records = input("How many records you want? : ")
        for i in range(int(records)):
            np.random.seed(i)
            s.__init__()
            while s.clock <= int(timer) :
                s.time_adv() 
            a=pd.Series([s.clock/s.num_arrivals,s.dep_sum1/s.num_of_departures1,s.dep_sum2/s.num_of_departures2,s.dep_sum1/s.clock,\
                        s.dep_sum2/s.clock,s.number_in_queue,s.total_wait_time,s.lost_customers],index=df.columns)
            df=df.append(a,ignore_index=True)   
            

        dfi.export(df, 'exponential.png')
        with open("exponential.png", "rb") as img_file:
            my_string = base64.b64encode(img_file.read())


        avg_teller_1 = df["Utilization teller 1"].mean()
        avg_teller_2 = df["Utilization teller 2"].mean()
        number_people = df["People who had to wait in line"].sum()
        avg_wait = df["Total average wait time"].mean()
        avg_lost = df["Lost Customers"].mean()


        thisdict = {
        "UTILIZATION OF TELLER 1 : ": avg_teller_1*100,
        "UTILIZATION OF TELLER 2 : ": avg_teller_2*100,
        "NUMBER OF PEOPLE WHO HAD TO WAIT : " : number_people,
        "AVERAGE WAIT TIME PER CUSTOMER : " : avg_wait*100,
        "AVERAGE LOST CUSTOMERS : " : avg_lost*100 }

        result = pd.DataFrame.from_dict(thisdict, orient = 'index')
        dfi.export(result, 'RESULTS.png')

        return my_string

    except Exception as e:
        print(e)
        print("Exception in Exponential Distribution")

@app.post('/Normal_distribution') 
async def Normal(timer: int = Form(...), records: int = Form(...)):
    try:
        s=Normal_distribution.Bank_Simulation()
        df=pd.DataFrame(columns=['Average interarrival time','Average service time teller1','Average service time teller 2','Utilization teller 1','Utilization teller 2',\
            'People who had to wait in line','Total average wait time','Lost Customers'])

        # timer = input("Enter Duration : ")
        # records = input("How many records you want? : ")
        for i in range(int(records)):
            np.random.seed(i)
            s.__init__()
            while s.clock <= int(timer) :
                s.time_adv() 
            a=pd.Series([s.clock/s.num_arrivals,s.dep_sum1/s.num_of_departures1,s.dep_sum2/s.num_of_departures2,s.dep_sum1/s.clock,\
                        s.dep_sum2/s.clock,s.number_in_queue,s.total_wait_time,s.lost_customers],index=df.columns)
            df=df.append(a,ignore_index=True)   

        dfi.export(df, 'normal.png')
        with open("normal.png", "rb") as img_file:
            my_string = base64.b64encode(img_file.read())

        avg_teller_1 = df["Utilization teller 1"].mean()
        avg_teller_2 = df["Utilization teller 2"].mean()
        number_people = df["People who had to wait in line"].sum()
        avg_wait = df["Total average wait time"].mean()
        avg_lost = df["Lost Customers"].mean()


        thisdict = {
        "UTILIZATION OF TELLER 1 : ": avg_teller_1*100,
        "UTILIZATION OF TELLER 2 : ": avg_teller_2*100,
        "NUMBER OF PEOPLE WHO HAD TO WAIT : " : number_people,
        "AVERAGE WAIT TIME PER CUSTOMER : " : avg_wait*100,
        "AVERAGE LOST CUSTOMERS : " : avg_lost*100 }

        result = pd.DataFrame.from_dict(thisdict, orient = 'index')
        dfi.export(result, 'RESULTS.png')

        return my_string
    except Exception as e:
        print(e)
        print("Exception in Normal Distribution")