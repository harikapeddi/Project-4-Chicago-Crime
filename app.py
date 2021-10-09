# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import pickle as p
import pandas as pd


app = Flask(__name__)
# app = Flask(__name__, template_folder='app')


# Load the model
# model = pickle.load(open('Model- sav/logisticregression.pickle','rb'))
# print(model)

# Load the model
model = p.load(open('Model- sav/logisticregression.sav','rb'))
print(model)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/api")
# def api_list():
#     """List all available api routes."""
#     return (
#         f"Available Routes:<br>"
#         f"Here goes some api"
    # )

@app.route("/model")
def model_results():
    return render_template('model.html')


@app.route("/stats")
def stats():
    return render_template("stats.html")


@app.route('/results/<crime>/<location>/<season>/<hour>/<lat>/<lon>/<domestic>')
def results(crime,location,season,hour,lat,lon,domestic):
    in_data = {
                'Domestic': 0.0,
                'Latitude': 0.0,
                'Longitude': 0.0,
                'Location Description_AIRPORT': 0.0,
                'Location Description_CHURCH': 0.0,
                'Location Description_COMMERCIAL BUILDING': 0.0,
                'Location Description_CTA': 0.0,
                'Location Description_EDUCATIONAL BUILDING': 0.0,
                'Location Description_FEDERAL PROPERTY': 0.0,
                'Location Description_HOSPITAL': 0.0,
                'Location Description_HOTEL': 0.0,
                'Location Description_OTHER': 0.0,
                'Location Description_PUBLIC ENTERTAINMENT': 0.0,
                'Location Description_PUBLIC OPEN SPACE': 0.0,
                'Location Description_RESIDENCE': 0.0,
                'Location Description_VEHICLE': 0.0,
                'Primary Type_ARSON': 0.0,
                'Primary Type_ASSAULT': 0.0,
                'Primary Type_BATTERY': 0.0,
                'Primary Type_BURGLARY': 0.0,
                'Primary Type_CRIM SEXUAL ASSAULT': 0.0,
                'Primary Type_CRIMINAL DAMAGE': 0.0,
                'Primary Type_CRIMINAL SEXUAL ASSAULT': 0.0,
                'Primary Type_CRIMINAL TRESPASS': 0.0,
                'Primary Type_DECEPTIVE PRACTICE': 0.0,
                'Primary Type_GAMBLING': 0.0,
                'Primary Type_HOMICIDE': 0.0,
                'Primary Type_INTERFERENCE WITH PUBLIC OFFICER': 0.0,
                'Primary Type_INTIMIDATION': 0.0,
                'Primary Type_KIDNAPPING': 0.0,
                'Primary Type_LIQUOR LAW VIOLATION': 0.0,
                'Primary Type_MOTOR VEHICLE THEFT': 0.0,
                'Primary Type_NARCOTICS': 0.0,
                'Primary Type_OFFENSE INVOLVING CHILDREN': 0.0,
                'Primary Type_OTHER': 0.0,
                'Primary Type_OTHER OFFENSE': 0.0,
                'Primary Type_PROSTITUTION': 0.0,
                'Primary Type_PUBLIC PEACE VIOLATION': 0.0,
                'Primary Type_ROBBERY': 0.0,
                'Primary Type_SEX OFFENSE': 0.0,
                'Primary Type_STALKING': 0.0,
                'Primary Type_THEFT': 0.0,
                'Primary Type_WEAPONS VIOLATION': 0.0,
                'HOUR_Afternoon': 0.0,
                'HOUR_Evening': 0.0,
                'HOUR_Morning': 0.0,
                'HOUR_Night': 0.0,
                'SEASON_Autumn': 0.0,
                'SEASON_Spring': 0.0,
                'SEASON_Summer': 0.0,
                'SEASON_Winter': 0.0}
    # print(model)
    crime = "Primary Type_"+crime.upper()
    location = "Location Description_"+location.upper()
    season = "SEASON_"+season.title()
    hour = "HOUR_"+hour.title()
    lat = float(lat)
    lon = float(lon)
    domestic=bool(domestic)

    in_data[crime] = 1.0
    in_data[location] = 1.0
    in_data[season] = 1.0
    in_data[hour] = 1.0
    in_data['Domestic'] = domestic
    in_data['Longitude'] = lon
    in_data['Latitude'] = lat


    data = np.array([x for x in in_data.values()]).reshape(1,-1)

    print(data)
    
    # data = np.array([crime,location,season,hour,lat,lon,domestic]).reshape(1,-1)
    output = model.predict(data)
    prob = model.predict_proba(data)
    print(prob)
    
    return jsonify({'result': output.tolist(), 'prob': prob.tolist()})


if __name__ == "__main__":
    app.run(debug=True)