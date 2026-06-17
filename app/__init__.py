import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Pages shown in the nav bar (label + route endpoint)
PAGES = [
    {"name": "Home", "endpoint": "index"},
    {"name": "Experience", "endpoint": "experience"},
    {"name": "Hobbies", "endpoint": "hobbies"},
    {"name": "Travel", "endpoint": "travel"},
]


ABOUT = (
    "I'm Tarek, a software engineer and researcher based in Vancouver. My work sits at the "
    "intersection of AI and systems software, with a focus on Rust, software security, and "
    "developer tooling. I enjoy building practical tools, contributing to open source, and "
    "exploring how AI can help solve challenging engineering problems."
)


WORK = [
    {"place": "Microsoft Research", "role": "Research Intern"},
    {"place": "MLH @ Meta", "role": "Software Engineering Fellow"},
    {"place": "Dell Technologies", "role": "Intern"},
    {"place": "Vodafone", "role": "Intern"},
]


EDUCATION = [
    {"school": "Mansoura University", "degree": "Bachelor's Degree in Computer Engineering and Systems"},
    {"school": "Simon Fraser University", "degree": "Master of Science in Computing Science"},
]


HOBBIES = [
    {"name": "Swimming", "image": "img/swimming.jpg"},
]


@app.context_processor
def inject_pages():
    return {"pages": PAGES, "url": os.getenv("URL")}


@app.route('/')
def index():
    return render_template('index.html', title="Tarek Elsayed", about=ABOUT)


@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience", work=WORK, education=EDUCATION)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", hobbies=HOBBIES)


@app.route('/travel')
def travel():
    return render_template('travel.html', title="Travel")
