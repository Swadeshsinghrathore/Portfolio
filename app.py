from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── Portfolio Data ──────────────────────────────────────────────
portfolio_data = {
    "name": "Swadesh Singh Rathore",
    "title": "AI & Data Science Enthusiast",
    "tagline": "Building intelligent systems with strong mathematical foundations and real-world impact.",
    "email": "ssrathore1922@gmail.com",
    "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore",
    "github": "https://github.com/swadeshsinghrathore",   # update if needed
    "available": True,

    "about": {
        "bio": "Artificial Intelligence focused Computer Science undergraduate with strong academic performance (CGPA 8.89/10) and deep interest in Machine Learning, Computer Vision, and Data Science. Experienced in developing ML-based systems, implementing predictive models, and working with structured and unstructured datasets using Python..",
        "stats": [
            {"num": "8.89", "label": "CGPA"},
            {"num": "3+", "label": "Projects"},
            {"num": "10+", "label": "Certifications"},
            {"num": "∞", "label": "Curiosity"},
        ]
    },

    "skills": [
        {"icon": "🐍", "name": "Python", "level": 90},
        {"icon": "🤖", "name": "Machine Learning", "level": 85},
        {"icon": "🧠", "name": "Computer Vision", "level": 80},
        {"icon": "📊", "name": "Data Analysis (Pandas, NumPy)", "level": 85},
        {"icon": "🔥", "name": "TensorFlow / OpenCV", "level": 80},
        {"icon": "🌐", "name": "Flask / Web Development", "level": 75},
        {"icon": "🗄️", "name": "MySQL / SQLite", "level": 80},
        {"icon": "🛠️", "name": "Git / GitHub", "level": 75},
    ],

    "projects": [
        {
            "num": "001(Ongoing)",
            "name": "Smart Crop Advisory System",
            "desc": "Machine learning-based advisory system assisting farmers in crop selection, irrigation planning, and pest control using soil and weather data. Implemented data preprocessing and predictive modeling for real-time agricultural recommendations.",
            "tags": ["HTML","css","JS","Flask","Python", "Data Preprocessing","...."],
            "link": "#"
        },
        {
            "num": "002",
            "name": "Resume Builder & ATS Checker",
            "desc": "Web-based resume platform built using Flask, MySQL, HTML, CSS, and JavaScript. Implemented ATS scoring system using structured keyword analysis and optimized database schema for efficient resume storage and retrieval.",
            "tags": ["HTML","css","JS","Bootstrap","Flask", "MySQL", "SQLite"],
            "link": "https://resumebuilder-hwar.onrender.com"
        },
        {
            "num": "003",
            "name": "Student Portfolio Website",
            "desc": "Personal portfolio website showcasing projects, skills, and experience. Developed using Flask for backend and HTML/CSS/JS for frontend, with structured data management to enable easy updates and scalability.",
            "tags": ["HTML","css","JS","Flask","Python"],
            "link": "https://portfolio-1-ct6h.onrender.com"
        },
        {
            "num": "004(Team)",
            "name": "Vision Voice (Assistive AI System)",
            "desc": "AI-based assistive system integrating sign language recognition, speech-to-text conversion, and object detection. Built real-time workflows using TensorFlow and OpenCV with structured dataset preparation.",
            "tags": ["TensorFlow", "OpenCV", "Computer Vision"],
            "link": "#"
        },
        
    ],

    "education": [
        {
            "degree": "B.Tech (Honours) — Computer Science (Artificial Intelligence)",
            "school": "Swami Keshvanand Institute of Technology (SKIT), Jaipur",
            "grade": "CGPA: 8.89/10",
            "year": "2023 — 2027",
            "marksheet": "marksheets/bt.pdf"
        },
        {
            "degree": "High School (PCM)",
            "school": "SBS Convent School, Sikar",
            "grade": "78.60%",
            "year": "2022",
            "marksheet": "marksheets/12.pdf"
          
        },
        {
            "degree": "Secondary School (10th)",
            "school": "SBS Convent School, Sikar",
            "grade": "81.20%",
            "year": "2020",
              "marksheet": "marksheets/10.pdf"
        }
    ],

    "experience": [
        {
            "role": "Technical Intern",
            "company": "Modern Insulators Ltd.",
            "duration": "May 2025 — August 2025",
            "location": "Abu, Rajasthan",
            "details": "Worked on machine learning model implementation, data preprocessing, and agricultural prediction system development."
        },
        {
            "role": "Web Designer", 
            "company": "MechaCraft Technologies Pvt. Ltd.",
            "duration": "June 2024 — November 2024",
            "location": "Jaipur, Rajasthan",
            "details": "Developed and maintained web systems, improved backend data handling, and implemented FAQ module to enhance usability."
        },
        {
            "role": "Web Development Intern",
            "company": "Kistechnosoftware Pvt. Ltd.",
            "duration": "May 2024 — June",
            "location": "Jaipur, Rajasthan",
            "details": "Developed responsive web applications using HTML, CSS, JavaScript and integrated MySQL databases."
        }
    ],

    "certifications": [
        "5X NPTEL Certifications",
        "Applied NLP Workshop - SKIT",
        "Career Essentials in Generative AI (Microsoft & LinkedIn)",
        "Geodata Processing using Python and ML - IIRS ISRO",
        "Web Development Internship Certification"
    ],

    "achievements": [
        "Student Coordinator — IIRS ISRO Outreach Program (SKIT)",
        "Preliminary Round Qualifier — Smart India Hackathon (SIH)",
        "Hackathon Participant — MUJHACKX 2.0"
    ]
}

# ── Routes ──────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", data=portfolio_data)

@app.route("/api/contact", methods=["POST"])
def contact():
    """Simple contact endpoint — extend with email/SMTP as needed."""
    body = request.get_json()
    name    = body.get("name", "").strip()
    email   = body.get("email", "").strip()
    message = body.get("message", "").strip()

    if not name or not email or not message:
        return jsonify({"success": False, "error": "All fields are required."}), 400

    print(f"[Contact] From: {name} <{email}>\nMessage: {message}")

    return jsonify({"success": True, "message": "Thanks! I'll get back to you soon."})

# ── Run ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)