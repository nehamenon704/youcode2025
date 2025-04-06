import os
from supabase import create_client, Client
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app=FastAPI()

origins=["http://127.0.0.1:8000"]

app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

url= "https://qmjiokvggswguqdlkczg.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtamlva3ZnZ3N3Z3VxZGxrY3pnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM4OTA3MzYsImV4cCI6MjA1OTQ2NjczNn0.qyShKKfFNWy84GPRS50l65mwA-B7GYn09nnRAz8hwaw"
supabase: Client = create_client(url, key)

response = (
    supabase.table("SampleDatabase")
    .select("*")
    .execute()
)

#Create a function to read all of the table entries and display them
@app.get("/", response_class=HTMLResponse)
def read_all_orgs(request:Request): 
    response = (
    supabase.table("SampleDatabase")
    .select("*")
    .execute())
    data = response.data
    return templates.TemplateResponse("display_data.html", {"request": request, "data": data})

@app.post("/submit2", response_class=HTMLResponse)
def read_all_orgs(request:Request): 
    response = (
    supabase.table("SampleDatabase")
    .select("*")
    .execute())
    data = response.data
    return templates.TemplateResponse("submit.html", {"request": request, "data": data})

@app.get("/insert", response_class=HTMLResponse)
def go_to_submit_page(request:Request):
        return templates.TemplateResponse("insert.html", {"request": request})


#Create a function to insert a table entry
@app.post("/submit", response_class=HTMLResponse)
def insert_org(request:Request, name:str= Form(...), s= Form(...), w= Form(...),
    loc= Form(...),
    info= Form(...)):
    # response=supabase.table("SampleDatabase").insert({
    # "Name": name,
    # "Strengths": s, 
    # "Weaknesses":w, 
    # "Location":loc, 
    # "Information":info
    # }).execute()
    # data = name
    return templates.TemplateResponse("index.html", {"request": request, "data":name})




#Create a function to find a match 
def find_match(company_name): 
    target_weakness=supabase.table("SampleDatabase").select('Weaknesses').eq('Name', company_name).execute()
    obtain_weakness_string=target_weakness.data[0]['Weaknesses']
    match=supabase.table("SampleDatabase").select("Name").eq("Strengths", obtain_weakness_string).execute().data[0]['Name']
    print(match)





# if __name__=="__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

    
  