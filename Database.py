import os
from supabase import create_client, Client


url= "https://qmjiokvggswguqdlkczg.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtamlva3ZnZ3N3Z3VxZGxrY3pnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM4OTA3MzYsImV4cCI6MjA1OTQ2NjczNn0.qyShKKfFNWy84GPRS50l65mwA-B7GYn09nnRAz8hwaw"
supabase: Client = create_client(url, key)

response = (
    supabase.table("SampleDatabase")
    .select("*")
    .execute()
)

#Create a function to read all of the table entries and display them
def read_all_orgs(): 
    response = (
    supabase.table("SampleDatabase")
    .select("*")
    .execute())


#Create a function to insert a table entry
def insert_org(name, strength, weakness):
    supabase.table("SampleDatabase").insert({
    "Name": name,
    "Strengths": strength, 
    "Weaknesses":weakness
}).execute()
    
#Create a function to find a match 
# def find_match()

insert_org("Youcode", "Talking", "Coding")



    
