import os
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     host=os.getenv("MYSQL_HOST"),
                     port=3306)

print(mydb)


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
    {"name": "Projects", "url": "/projects"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Travel", "url": "/travel"},
    {"name": "Timeline", "url": "/timeline"},
]

NAME = "Esosa Ohangbon"
TAGLINE = "Software engineer, student at Carleton University."

WORK = [
    {
        "place": "Shopify",
        "role": "Infrastructure Engineer Intern",
        "dates": "Incoming Fall 2026",
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

HOBBIES = [
    {"name": "Open Source", "image": None},
    {"name": "Chess", "image": None},
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
}


@app.context_processor
def inject_globals():
    return {"url": os.getenv("URL"), "pages": PAGES, "name": NAME,
            "tech_icons": TECH_ICONS}


@app.route('/')
def index():
    return render_template('index.html', title=NAME, tagline=TAGLINE,
                           work=WORK, education=EDUCATION,
                           profile_img="img/EsosaOhangbon.jpg")


@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects",
                           projects=PROJECTS)


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies",
                           hobbies=HOBBIES)


@app.route('/travel')
def travel():
    return render_template('travel.html', title="Travel",
                           map_img="img/esosa_visited_map.png")


@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline")


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
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
