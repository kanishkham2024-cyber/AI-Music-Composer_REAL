HEAD
from fastapi import FastAPI, Query, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from music_generator import generate_music  # Only if this file exists

app = FastAPI()

# Home route
@app.get("/")
def root():
    return {"message": "AI Music Composition Tool is running"}

# GET method to generate music and return a file
@app.get("/generate")
def generate(
    genre: str = Query("classical"),
    mood: str = Query("happy"),
    tempo: int = Query(120)
):
    output_file = generate_music(genre, mood, tempo)
    return FileResponse(output_file, media_type='audio/midi', filename='generated_music.mid')

# POST method for JSON-based music generation
class MusicRequest(BaseModel):
    genre: str
    mood: str
    tempo: int

@app.post("/compose")
def compose_music(request: MusicRequest):
    # Replace with real generation later
    return {
        "status": "success",
        "message": f"Generating a {request.mood} {request.genre} track at {request.tempo} BPM."
    }


from fastapi import FastAPI, Query, Request
from fastapi.responses import FileResponse
from pydantic import BaseModel
from music_generator import generate_music  # Only if this file exists

app = FastAPI()

# Home route
@app.get("/")
def root():
    return {"message": "AI Music Composition Tool is running"}

# GET method to generate music and return a file
@app.get("/generate")
def generate(
    genre: str = Query("classical"),
    mood: str = Query("happy"),
    tempo: int = Query(120)
):
    output_file = generate_music(genre, mood, tempo)
    return FileResponse(output_file, media_type='audio/midi', filename='generated_music.mid')

# POST method for JSON-based music generation
class MusicRequest(BaseModel):
    genre: str
    mood: str
    tempo: int

@app.post("/compose")
def compose_music(request: MusicRequest):
    # Replace with real generation later
    return {
        "status": "success",
        "message": f"Generating a {request.mood} {request.genre} track at {request.tempo} BPM."
    }


