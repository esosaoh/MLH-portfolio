import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


# --- Tarek's data ---

TAREK_PAGES = [
    {"name": "Home", "url": "/tarek/"},
    {"name": "Experience", "url": "/tarek/experience"},
    {"name": "Hobbies", "url": "/tarek/hobbies"},
    {"name": "Travel", "url": "/tarek/travel"},
]

TAREK_ABOUT = (
    "I'm Tarek, a software engineer and researcher based in Vancouver. My work sits at the "
    "intersection of AI and systems software, with a focus on Rust, software security, and "
    "developer tooling. I enjoy building practical tools, contributing to open source, and "
    "exploring how AI can help solve challenging engineering problems."
)

TAREK_WORK = [
    {"place": "Microsoft Research", "role": "Research Intern"},
    {"place": "MLH @ Meta", "role": "Software Engineering Fellow"},
    {"place": "Dell Technologies", "role": "Intern"},
    {"place": "Vodafone", "role": "Intern"},
]

TAREK_EDUCATION = [
    {"school": "Mansoura University", "degree": "Bachelor's Degree in Computer Engineering and Systems"},
    {"school": "Simon Fraser University", "degree": "Master of Science in Computing Science"},
]

TAREK_HOBBIES = [
    {"name": "Swimming", "image": "img/swimming.jpg"},
]


# --- Esosa's data ---

ESOSA_PAGES = [
    {"name": "Home", "url": "/esosa/"},
    {"name": "Experience", "url": "/esosa/experience"},
    {"name": "Hobbies", "url": "/esosa/hobbies"},
    {"name": "Travel", "url": "/esosa/travel"},
]

ESOSA_ABOUT = (
    "I'm Esosa, a Software Engineering student at Carleton University who enjoys building "
    "scalable systems and solving tough problems. My interests span cloud infrastructure, "
    "distributed systems, compilers, and open source development."
)

ESOSA_WORK = [
    {"place": "Major League Hacking", "role": "Production Engineering Fellow"},
    {"place": "RBC", "role": "Software Engineer Intern"},
    {"place": "Google Summer of Code", "role": "Open Source Developer (CNCF)"},
    {"place": "Carleton HealthVisFutures Lab", "role": "Research Assistant"},
]

ESOSA_EDUCATION = [
    {"school": "Carleton University", "degree": "Bachelor's Degree in Software Engineering"},
]

ESOSA_HOBBIES = [
    {"name": "Open Source", "image": None},
    {"name": "Chess", "image": None},
]


@app.context_processor
def inject_url():
    return {"url": os.getenv("URL")}


# --- Landing page ---

@app.route('/')
def landing():
    return render_template('landing.html', title="Portfolio")


# --- Tarek's routes ---

@app.route('/tarek/')
def tarek_index():
    return render_template('index.html', title="Tarek Elsayed",
                           about=TAREK_ABOUT, pages=TAREK_PAGES,
                           profile_img="img/TarekElsayed.jpg")


@app.route('/tarek/experience')
def tarek_experience():
    return render_template('experience.html', title="Experience",
                           work=TAREK_WORK, education=TAREK_EDUCATION,
                           pages=TAREK_PAGES)


@app.route('/tarek/hobbies')
def tarek_hobbies():
    return render_template('hobbies.html', title="Hobbies",
                           hobbies=TAREK_HOBBIES, pages=TAREK_PAGES)


@app.route('/tarek/travel')
def tarek_travel():
    return render_template('travel.html', title="Travel", pages=TAREK_PAGES, map_img="img/visited_map.png")


# --- Esosa's routes ---

@app.route('/esosa/')
def esosa_index():
    return render_template('index.html', title="Esosa Ohangbon",
                           about=ESOSA_ABOUT, pages=ESOSA_PAGES,
                           profile_img="img/EsosaOhangbon.jpg")


@app.route('/esosa/experience')
def esosa_experience():
    return render_template('experience.html', title="Experience",
                           work=ESOSA_WORK, education=ESOSA_EDUCATION,
                           pages=ESOSA_PAGES)


@app.route('/esosa/hobbies')
def esosa_hobbies():
    return render_template('hobbies.html', title="Hobbies",
                           hobbies=ESOSA_HOBBIES, pages=ESOSA_PAGES)


@app.route('/esosa/travel')
def esosa_travel():
    return render_template('travel.html', title="Travel", pages=ESOSA_PAGES, map_img="img/esosa_visited_map.png")
