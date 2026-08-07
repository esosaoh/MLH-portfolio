import os
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                         user=os.getenv("MYSQL_USER"),
                         password=os.getenv("MYSQL_PASSWORD"),
                         host=os.getenv("MYSQL_HOST"),
                         port=3306)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])


PAGES = [
    {"name": "Experience", "url": "/experience"},
    {"name": "Projects", "url": "/projects"},
    {"name": "Travel", "url": "/travel"},
    {"name": "Timeline", "url": "/timeline"},
]

NAME = "Esosa Ohangbon"
TAGLINE = "Software engineer, student at Carleton University."

ABOUT_INTRO = "Third year software engineering student at Carleton University."
ABOUT_POINTS = [
    "I like open source and building things that ship.",
    "Currently a Production Engineering Fellow at MLH.",
]

GITHUB_URL = "https://github.com/esosaoh"
LINKEDIN_URL = os.getenv("LINKEDIN_URL", "https://linkedin.com/in/ohangbon")

WORK = [
    {
        "place": "Shopify",
        "role": "Software Engineer Intern",
        "dates": "Incoming Fall 2026",
        "description": "Database Platform team, working on Core MySQL.",
        "tech": [],
        "logo": "img/logos/shopify.png",
    },
    {
        "place": "RBC",
        "role": "Software Engineer Intern",
        "dates": "Sep. 2025 - Present",
        "description": "GitHub Enterprise migration and CI/CD tooling for RBC's developer platform.",
        "tech": ["TypeScript", "GitHub Actions", "MongoDB", "RabbitMQ", "Terraform", "HashiCorp Vault"],
        "logo": "img/logos/rbc.png",
    },
    {
        "place": "Major League Hacking",
        "role": "Production Engineering Fellow",
        "dates": "Jun. 2026 - Present",
        "description": "SRE and Production Engineering, in collaboration with Meta.",
        "tech": ["Python", "Flask", "Docker", "Nginx"],
        "logo": "img/logos/mlh.svg",
    },
    {
        "place": "Google Summer of Code",
        "role": "Open Source Developer (CNCF)",
        "dates": "May 2025 - Sep. 2025",
        "description": "TypeScript SDK for writing Kubernetes cluster admission policies.",
        "tech": ["TypeScript", "Kubernetes", "WebAssembly"],
        "logo": "img/logos/gsoc.png",
    },
    {
        "place": "Carleton University",
        "role": "Undergraduate Research Assistant",
        "dates": "May 2024 - Dec. 2024",
        "description": "Evaluated physician accuracy for cardiac radio-ablation therapy (CRA).",
        "tech": ["Python"],
        "logo": "img/logos/carleton.png",
    },
]

EDUCATION = [
    {
        "school": "Carleton University",
        "degree": "Bachelor of Engineering in Software Engineering",
        "dates": "Sep. 2023 - Apr. 2028",
        "logo": "img/logos/carleton.png",
    },
]

# Places visited, plotted as pins on a live OpenStreetMap.
VISITED_PLACES = [
    {"name": "Dubai, UAE", "lat": 25.2048, "lng": 55.2708},
    {"name": "Abu Dhabi, UAE", "lat": 24.4539, "lng": 54.3773},
    {"name": "Lagos, Nigeria", "lat": 6.5244, "lng": 3.3792},
    {"name": "Ottawa, Canada", "lat": 45.4215, "lng": -75.6972},
    {"name": "Toronto, Canada", "lat": 43.6532, "lng": -79.3832},
    {"name": "Dallas, USA", "lat": 32.7767, "lng": -96.7970},
    {"name": "Houston, USA", "lat": 29.7604, "lng": -95.3698},
    {"name": "Rome, Italy", "lat": 41.9028, "lng": 12.4964},
    {"name": "London, UK", "lat": 51.5074, "lng": -0.1278},
    {"name": "Ghana", "lat": 7.9465, "lng": -1.0232},
    {"name": "Florida, USA", "lat": 27.6648, "lng": -81.5158},
]

PROJECTS = [
    {
        "name": "Playlifts",
        "description": "A playlist transfer platform for Spotify and YouTube Music. ~200 users in the first week.",
        "tech": ["React", "TypeScript", "Flask", "Celery", "Redis", "Docker"],
        "demo": "https://playlifts.com",
        "github": "https://github.com/esosaoh/Playlifts",
    },
    {
        "name": "kubewarden/policy-sdk-js",
        "description": "A JavaScript (and TypeScript) SDK for Kubewarden policies.",
        "tech": ["TypeScript", "Kubernetes", "WebAssembly", "npm"],
        "demo": None,
        "github": "https://github.com/kubewarden/policy-sdk-js",
    },
    {
        "name": "GitMentor",
        "description": "An AI assistant for open-source contributors. Winner at cuHacking 6.",
        "tech": ["Next.js", "TypeScript", "Python", "Flask", "Gemini API"],
        "demo": "https://gitmentor.co",
        "github": "https://github.com/esosaoh/git-mentor",
    },
    {
        "name": "dodo",
        "description": "Fast and accurate website link checker.",
        "tech": ["Go", "SQLite"],
        "demo": None,
        "github": "https://github.com/esosaoh/dodo",
    },
    {
        "name": "ferrum",
        "description": "Distributed message broker (Apache Kafka clone).",
        "tech": ["Rust", "Tokio"],
        "demo": None,
        "github": "https://github.com/esosaoh/ferrum",
    },
    {
        "name": "Budgetify",
        "description": "A containerized budget tracking API.",
        "tech": ["Java", "Spring Boot", "PostgreSQL", "Docker"],
        "demo": None,
        "github": "https://github.com/esosaoh/budgetify",
    },
    {
        "name": "Compressr",
        "description": "An implementation of the Huffman encoding algorithm for file compression.",
        "tech": ["C++", "CMake", "Google Test"],
        "demo": None,
        "github": "https://github.com/esosaoh/compressr",
    },
    {
        "name": "Carleton Courses",
        "description": "A redesigned Carleton student portal. Built at Hack The Tunnels 2024.",
        "tech": ["React", "TypeScript", "Node.js", "SCSS", "Prisma"],
        "demo": None,
        "github": "https://github.com/esosaoh/hack-the-tunnels",
    },
]


# Maps a tech name to its icon in static/img/tech/ (Simple Icons).
# Techs without an entry fall back to a letter chip.
TECH_ICONS = {
    "Python": "python.svg",
    "Flask": "flask.svg",
    "Docker": "docker.svg",
    "Nginx": "nginx.svg",
    "Node.js": "nodedotjs.svg",
    "Express": "express.svg",
    "MongoDB": "mongodb.svg",
    "RabbitMQ": "rabbitmq.svg",
    "Terraform": "terraform.svg",
    "HashiCorp Vault": "vault.svg",
    "React": "react.svg",
    "GitHub Actions": "githubactions.svg",
    "TypeScript": "typescript.svg",
    "Kubernetes": "kubernetes.svg",
    "WebAssembly": "webassembly.svg",
    "Celery": "celery.svg",
    "Redis": "redis.svg",
    "npm": "npm.svg",
    "Next.js": "nextdotjs.svg",
    "Gemini API": "googlegemini.svg",
    "Java": "openjdk.svg",
    "Spring Boot": "springboot.svg",
    "PostgreSQL": "postgresql.svg",
    "C++": "cplusplus.svg",
    "CMake": "cmake.svg",
    "SCSS": "sass.svg",
    "Prisma": "prisma.svg",
    "Go": "go.svg",
    "Rust": "rust.svg",
    "SQLite": "sqlite.svg",
    "Tokio": "tokio.svg",
}


@app.context_processor
def inject_globals():
    return {"url": os.getenv("URL"), "pages": PAGES, "name": NAME,
            "tech_icons": TECH_ICONS}


@app.route('/')
def index():
    return render_template('index.html', title=NAME, tagline=TAGLINE,
                           about_intro=ABOUT_INTRO, about_points=ABOUT_POINTS,
                           github_url=GITHUB_URL, linkedin_url=LINKEDIN_URL,
                           profile_img="img/EsosaOhangbon.jpg")


@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience",
                           work=WORK, education=EDUCATION)


@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects",
                           projects=PROJECTS)


@app.route('/travel')
def travel():
    return render_template('travel.html', title="Travel",
                           visited=VISITED_PLACES)


@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    content = request.form.get('content', '').strip()

    if not name:
        return 'Invalid name', 400
    if not content:
        return 'Invalid content', 400
    if '@' not in email or '.' not in email.split('@')[-1]:
        return 'Invalid email', 400

    timeline_post = TimelinePost.create(name=name, email=email,
                                        content=content)
    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p) for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_time_line_post(post_id):
    deleted = TimelinePost.delete().where(
        TimelinePost.id == post_id).execute()
    if deleted == 0:
        return {'error': f'timeline post {post_id} not found'}, 404
    return {'deleted': post_id}
