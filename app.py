from flask import Flask, jsonify,request
import ipl
app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/api/teams")
def teams():
    teams = ipl.teamaAPI()
    return jsonify(teams)

@app.route("/api/teamvteam")
def teamvteam():
    team1=request.args.get("team1")
    team2=request.args.get("team2")
    response=ipl.teamVteamAPI(team1,team2)
    print(response)
    return jsonify(response)

app.run(debug=True)
