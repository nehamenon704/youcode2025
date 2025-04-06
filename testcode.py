from fastapi import FastAPI, Request
from supabase import create_client, Client

# Supabase setup
url = "https://qmjiokvggswguqdlkczg.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFtamlva3ZnZ3N3Z3VxZGxrY3pnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDM4OTA3MzYsImV4cCI6MjA1OTQ2NjczNn0.qyShKKfFNWy84GPRS50l65mwA-B7GYn09nnRAz8hwaw"
supabase: Client = create_client(url, key)

app = FastAPI()

# Root test route
@app.get("/")
def root():
    return {"message": "Hello from FastAPI with Supabase!"}

# Submit user info and get a match
@app.post("/submit")
async def submit_and_match(request: Request):
    data = await request.json()
    name = data.get("name")
    strength = data.get("strength")
    weakness = data.get("weakness")
    location = data.get("location")

    # Insert org into Supabase
    try:
        supabase.table("SampleDatabase").insert({
            "Name": name,
            "Strengths": strength,
            "Weaknesses": weakness,
            "Location": location
        }).execute()
    except Exception as e:
        return {"status": "error", "message": f"Insertion failed: {str(e)}"}

    # Fetch all orgs from Supabase
    all_orgs = supabase.table("SampleDatabase").select("*").execute().data

    # Convert weakness into a set for comparison
    user_weaknesses = set(map(str.strip, weakness.lower().split(",")))

    # Find a match
    for org in all_orgs:
        if org["Name"].lower() == name.lower():
            continue  # Skip current user

        org_strengths = set(map(str.strip, org["Strengths"].lower().split(",")))
        if user_weaknesses & org_strengths:
            return {"status": "match_found", "match": org}

    return {"status": "no_match", "message": "No suitable match found yet."}

