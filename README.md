# IPL API Service

A simple RESTful API service built with Python to serve IPL (Indian Premier League) data such as matches, teams, and players. This project demonstrates how to design and expose clean API endpoints that return cricket data in JSON format.

## ✨ Features
- Match Endpoints → Fetch list of matches, match details by ID
- Team Endpoints → Get team details, players list, stats
- Player Endpoints → Access player profiles and stats
- JSON Responses → Lightweight and ready for frontend integration
- Service Layer → Clean separation of routes and business logic

## 📂 Repository Contents
ipl-api-service/
├── app.py                # Main entry point (Flask/FastAPI server)
├── routes/
│   ├── matches.py        # Endpoints for matches
│   ├── teams.py          # Endpoints for teams
│   └── players.py        # Endpoints for players
├── services/
│   └── ipl_service.py    # Business logic (fetching / processing IPL data)
├── data/
│   └── ipl_data.json     # (Optional) Static IPL data file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

## ⚙️ Requirements
- Python 3.8+
- Install dependencies from requirements.txt

## 🚀 Getting Started
1. Clone the repository:
   git clone https://github.com/ranavikas1998/ipl-api-service.git
   cd ipl-api-service
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate      # On macOS/Linux
   venv\Scripts\activate         # On Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Run the server:
   python app.py
5. Open browser or API client (like Postman) at:
   http://127.0.0.1:5000/

## ▶️ Run the Application
Example API endpoints:
- Get All Matches → GET /api/matches
- Get Match by ID → GET /api/matches/1
- Get All Teams → GET /api/teams
- Get Team by Name/ID → GET /api/teams/MI
- Get Player by ID → GET /api/players/101

Example Response for /api/matches:
[
  {"id": 1, "team1": "MI", "team2": "CSK", "date": "2025-03-23"},
  {"id": 2, "team1": "RCB", "team2": "KKR", "date": "2025-03-24"}
]

## 🔍 How It Works
1. app.py → Starts the Flask/FastAPI server and registers all routes under /api/.
2. routes/ → Defines REST API endpoints for matches, teams, and players, forwards requests to the service layer.
3. services/ipl_service.py → Handles core logic: fetches IPL data (either from static JSON or external API) and returns processed Python dictionaries.
4. Response Layer → Flask converts dictionaries → JSON and returns response to API client.

## 📈 Example Project Flow
Client (Browser/Postman) → Request (/api/matches) → app.py → routes/matches.py → services/ipl_service.py → Fetch IPL Data → Return JSON Response

## 🚧 Future Enhancements
- Live IPL data integration from official APIs
- Player stats history & graphs
- Authentication (JWT) for premium APIs
- Dockerize the service for cloud deployment
- Swagger / Redoc API documentation

## 👤 Author
Vikas Rana  
GitHub: [ranavikas1998](https://github.com/ranavikas1998)

## 📜 License
This project is open-source. License details (MIT/Apache2) can be added in a LICENSE file.
