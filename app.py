from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ── Portfolio Data ──────────────────────────────────────────────
portfolio_data = {
    "name": "Swadesh Singh Rathore",
    "title": "AI & Data Engineering Enthusiast",
    "tagline": "Turning data into meaningful insights and building intelligent systems for real-world problems.",
    "email": "ssrathore1922@gmail.com",
    "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore",
    "github": "https://github.com/swadeshsinghrathore",   # update if needed
    "available": True,

    "about": {
        "bio": "Computer Science undergraduate (AI specialization) with strong academic performance (CGPA 9.00/10) and hands-on experience across Machine Learning, Data Engineering, and Quantum Computing. Built production-style data pipelines using PySpark, Azure ADF, and Delta Lake, and worked on quantum error mitigation research at DRDO SAG Lab using Qiskit on real IBM Quantum hardware. Comfortable turning both structured and unstructured data into working, deployable systems.",
        "stats": [
            {"num": "9.00", "label": "CGPA"},
            {"num": "7+", "label": "Projects"},
            {"num": "10+", "label": "Certifications"},
            {"num": "∞", "label": "Curiosity"},
        ]
    },

    "skills": [
    {
        "title": "Languages",
        "skills": [
            {"icon": "🐍", "name": "Python", "level": 85},
            {"icon": "💻", "name": "C / C++ / Java", "level": 75},
            {"icon": "🌐", "name": "JavaScript (Basic)", "level": 65},
            {"icon": "🗄️", "name": "SQL", "level": 80},
            {"icon": "📐", "name": "MATLAB", "level": 70}
        ]
    },
    {
        "title": "AI / Machine Learning",
        "skills": [
            {"icon": "🤖", "name": "Machine Learning", "level": 75},
            {"icon": "🔥", "name": "TensorFlow", "level": 70},
            {"icon": "🧠", "name": "Scikit-Learn", "level": 75},
            {"icon": "🧹", "name": "Data Preprocessing", "level": 80}
        ]
    },
    {
        "title": "Data Science & Analytics",
        "skills": [
            {"icon": "📊", "name": "Pandas / NumPy", "level": 85},
            {"icon": "📈", "name": "Data Analysis & EDA", "level": 80},
            {"icon": "📉", "name": "Matplotlib / Seaborn", "level": 75},
            {"icon": "📊", "name": "Statistical Analysis", "level": 70}
        ]
    },
    {
        "title": "Web Development & Databases",
        "skills": [
            {"icon": "🌍", "name": "Flask / Web Development", "level": 80},
            {"icon": "🗃️", "name": "MySQL / SQLite", "level": 80},
            {"icon": "🎨", "name": "HTML / CSS / Bootstrap / Figma", "level": 85}
        ]
    },
    {
        "title": "Tools & Platforms",
        "skills": [
            {"icon": "🛠️", "name": "Git / GitHub", "level": 80},
            {"icon": "📓", "name": "Jupyter / Google Colab", "level": 85},
            {"icon": "⚙️", "name": "VS Code / IntelliJ / Android Studio", "level": 80},
            {"icon": "🐍", "name": "Anaconda", "level": 75}
        ]
    },
    {
        "title": "Soft Skills",
        "skills": [
            {"icon": "🧠", "name": "Analytical Thinking", "level": 90},
            {"icon": "🧩", "name": "Problem Solving", "level": 90},
            {"icon": "🤝", "name": "Teamwork & Communication", "level": 85},
            {"icon": "🚀", "name": "Leadership & Adaptability", "level": 85}
        ]
    }
],

    "projects": [
        {
            "num": "001(Ongoing)",
            "name": "Smart Crop Advisory System",
            "desc": "Machine learning-based advisory system assisting farmers in crop selection, irrigation planning, and pest control using soil and weather data. Implemented data preprocessing and predictive modeling for real-time agricultural recommendations.",
            "long_desc": "This system provides a comprehensive, intelligent agricultural recommendation engine. By analyzing soil metrics, real-time weather forecasts, and historical crop data, it uses predictive machine learning models to suggest optimal crops, forecast precise irrigation schedules, and preemptively warn against likely pest outbreaks. This significantly boosts yield while reducing resource waste.",
            "tags": ["HTML","css","JS","Flask","Python", "Data Preprocessing","...."],
            "photos": [
                "image/1.png"
            ],
            "contributors": [
                {
                    "name": "Swadesh Singh Rathore",
                    "photo": "image/1.png",
                    "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore"
                }
            ],
            "link": "#"
        },
        {
            "num": "002",
            "name": "Resume Builder & ATS Checker",
            "desc": "Web-based resume platform built using Flask, MySQL, HTML, CSS, and JavaScript. Implemented ATS scoring system using structured keyword analysis and optimized database schema for efficient resume storage and retrieval.",
            "long_desc": "A fully responsive web platform designed to help job seekers build professional resumes while simultaneously analyzing them against Applicant Tracking Systems (ATS). The application parses the user's resume and job description, running keyword frequency algorithms to provide an actionable ATS score and improvement suggestions. Built with a robust Flask backend and MySQL for secure user data management.",
            "tags": ["HTML","css","JS","Bootstrap","Flask", "MySQL", "SQLite"],
            "photos": [
                 "image/1.png"
            ],
            "contributors": [
                {
                    "name": "Swadesh Singh Rathore",
                    "photo": "image/1.png",
                    "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore"
                }
            ],
            "link": "https://resumebuilder-hwar.onrender.com"
        },
        {
            "num": "003",
            "name": "Student Portfolio Website",
            "desc": "Personal portfolio website showcasing projects, skills, and experience. Developed using Flask for backend and HTML/CSS/JS for frontend, with structured data management to enable easy updates and scalability.",
            "long_desc": "A sleek, dark-themed digital portfolio crafted to showcase projects, skills, and academic achievements. It features a completely dynamic backend powered by Flask, meaning all content (projects, skills, education) is injected from structured data without hardcoding HTML. The frontend utilizes custom CSS variables, subtle micro-animations, and a highly responsive design system.",
            "tags": ["HTML","css","JS","Flask","Python"],
            "photos": [
                "image/1.png"
            ],
            "contributors": [
                {
                    "name": "Swadesh Singh Rathore",
                    "photo": "image/1.png",
                    "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore"
                }
            ],
            "link": "https://portfolio-1-ct6h.onrender.com"
        },
        {
            "num": "004(Team)",
            "name": "Vision Voice (Assistive AI System)",
            "desc": "AI-based assistive system integrating sign language recognition, speech-to-text conversion, and object detection. Built real-time workflows using TensorFlow and OpenCV with structured dataset preparation.",
            "long_desc": "Vision Voice aims to bridge communication gaps for the differently-abled. It employs deep learning computer vision models via OpenCV and TensorFlow to recognize sign language gestures in real-time and translate them into text/speech. Concurrently, it offers object detection and speech-to-text functionalities to assist visually or hearing impaired users navigate their environment.",
            "tags": ["TensorFlow", "OpenCV", "Computer Vision"],
            "photos": [
                 "image/1.png"
            ],
            "contributors": [
                {
                    "name": "Swadesh Singh Rathore",
                    "photo": "image/1.png",
                    "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore"
                },
                {
                    "name": "Team Member",
                    "photo": "image/1.png",
                    "linkedin": "#"
                }
            ],
            "link": "#"
        },
        {
    "num": "005",
    "name": "Online Bookstore & Library Data Warehouse",
    "desc": "Enterprise-grade data warehouse built during Celebal Technologies Data Engineering internship. Implemented medallion architecture (Bronze-Silver-Gold) in MySQL with watermark-based incremental loading and advanced SQL analytics.",
    "long_desc": "Designed and built a full-scale data warehouse for an online bookstore & library system following medallion architecture principles. Used watermark-based incremental loading to efficiently process only new/changed records instead of full reloads, cutting redundant processing. Implemented advanced SQL logic including window functions (LAG), CTEs, and self-joins for complex analytical transformations, and delivered 5 Gold-layer KPI views for business reporting. Also applied PySpark fundamentals, Delta Lake MERGE operations, and SCD Type 1/2 handling as part of the broader internship pipeline work.",
    "tags": ["PySpark", "Azure ADF", "Delta Lake", "MySQL", "SQL", "Medallion Architecture", "ETL"],
    "photos": [
        "image/5.png"
    ],
    "contributors": [
        {
            "name": "Swadesh Singh Rathore",
            "photo": "image/1.png",
            "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore"
        }
    ],
    "link": "#"
},
{
    "num": "006",
    "name": "QuantumBase — QEM & QEC Benchmarking Framework",
    "desc": "Quantum error mitigation and correction benchmarking framework built during DRDO SAG Lab internship. Evaluated multiple QEM techniques across a 7-circuit suite on real IBM Quantum hardware.",
    "long_desc": "Built a comprehensive benchmarking framework in Qiskit to evaluate Quantum Error Mitigation (QEM) techniques — TREX, Zero-Noise Extrapolation (ZNE), Probabilistic Error Cancellation (PEC), and Dynamical Decoupling — across a 7-circuit test suite (Bell, GHZ-3, GHZ-4, Mirror, QFT, Random Clifford, and Teleportation circuits) run on real IBM Quantum hardware. Also implemented Quantum Error Correction (QEC) codes including the 3-qubit bit-flip and phase-flip codes, with partial implementation of the Shor 9-qubit code, to study fidelity improvements under noise.",
    "tags": ["Qiskit", "Quantum Computing", "IBM Quantum", "Python", "QEM", "QEC"],
    "photos": [
        "image/6.png"
    ],
    "contributors": [
        {
            "name": "Swadesh Singh Rathore",
            "photo": "image/1.png",
            "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore"
        }
    ],
    "link": "#"
},{
    "num": "007",
    "name": "Smart Fraud Detection Pipeline",
    "desc": "Data engineering pipeline built on Databricks using Medallion Architecture (Bronze-Silver-Gold) to detect fraudulent bank transactions from accounts, transactions, and fraud watchlist data.",
    "long_desc": "Built an end-to-end fraud detection pipeline on Databricks following Medallion Architecture. Bronze layer ingested raw accounts, transactions, and fraud watchlist CSVs into Delta Tables with schema validation and null checks. Silver layer cleaned and standardized the data (trimming, case normalization, type casting, duplicate removal) and enriched transactions by left-joining them with account details. Gold layer applied fraud-flag logic by matching transactions against the fraud watchlist, then generated aggregated insights — fraud breakdown per account, fraud type, and branch — along with overall summary metrics. Processed 200 transactions across 50 accounts, flagging 26 as fraudulent (13% fraud rate) across 5 Gold-layer output tables.",
    "tags": ["PySpark", "Spark SQL", "Databricks", "Delta Lake", "Medallion Architecture", "Banking"],
    "photos": [
        "image/7.png"
    ],
    "contributors": [
        {
            "name": "Swadesh Singh Rathore",
            "photo": "image/1.png",
            "linkedin": "https://www.linkedin.com/in/swadeshsinghrathore"
        }
    ],
    "link": "#"
}
    ],

    "education": [
        {
            "degree": "B.Tech (Honours) — Computer Science (Artificial Intelligence)",
            "school": "Swami Keshvanand Institute of Technology (SKIT), Jaipur",
            "grade": "CGPA: 9.00/10",
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
            "role": "Data Engineering Intern",
            "company": "Celebal Technologies",
            "duration": "May 2026- July 2026",
            "location": "Jaipur(Remote)",
            "details": "Built enterprise data pipelines using PySpark and Azure ADF; implemented Delta Lake MERGE operations and SCD Type 1/2 handling; designed a medallion architecture data warehouse with watermark-based incremental loading and delivered various  Gold-layer KPI views."
        },
        {
            "role": "Quantum Computing Intern",
            "company": "DRDO SAG Lab, New Delhi",
            "duration": "May 2026- July 2026",
            "location": "New Delhi(Onsite)",
            "details": "Built a Quantum Error Mitigation (QEM) benchmarking framework in Qiskit covering TREX, ZNE, PEC, and Dynamical Decoupling across a 7-circuit suite on IBM Quantum hardware; implemented Quantum Error Correction (QEC) codes including 3-qubit bit-flip/phase-flip and Shor 9-qubit codes."
        },
        {
            "role": "Technical Intern",
            "company": "Modern Insulators Ltd.",
            "duration": "May 2025 — August 2025",
            "location": "Abu, Rajasthan(Onsite)",
            "details": "Worked on machine learning model implementation, data preprocessing, and agricultural prediction system development."
        },
        {
            "role": "Web Designer", 
            "company": "MechaCraft Technologies Pvt. Ltd.",
            "duration": "June 2024 — November 2024",
            "location": "Jaipur, Rajasthan(Onsite)",
            "details": "Developed and maintained web systems, improved backend data handling, and implemented FAQ module to enhance usability."
        },
        {
            "role": "Web Development Intern",
            "company": "Kistechnosoftware Pvt. Ltd.",
            "duration": "May 2024 — June",
            "location": "Jaipur, Rajasthan(Onsite)",
            "details": "Developed responsive web applications using HTML, CSS, JavaScript and integrated MySQL databases."
        }
    ],

    "certifications": [
            "7X NPTEL Certifications",
    "Career Essentials in Generative AI (Microsoft & LinkedIn)",
    "Introduction to Generative AI (AWS Training)",
    "Geodata Processing using Python and ML — IIRS, ISRO",
    "Space-Based Inputs for Village-Level Crop Assessment — ISRO",
    "Workshop on Basics of AI/ML — Cognizance, IIT Roorkee",
    "Web Development Internship Certification — KTSPL",
    "Applied NLP Workshop - SKIT"
    ],

    "achievements": [
        "Secured 100% scholarship in RCAT Rajasthan(2026)",
        "Earned NPTEL Elite Certificate in Programming in Java (2025)",
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