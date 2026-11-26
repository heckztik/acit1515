import json
from pathlib import Path
from uuid import uuid4

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

DATA_FILE = Path(__file__).with_name("tips.json")

def save_tips():
    DATA_FILE.write_text(json.dumps(tips, indent=2), encoding="utf-8")


# Initialize JSON

tips = [
    {"id": str(uuid4()), "text": "Read the error message carefully.", "likes": 0},
    {"id": str(uuid4()), "text": "Break problems into smaller steps.", "likes": 2},
]

if DATA_FILE.exists():
    with open(DATA_FILE) as file:
        tips = json.load(file)
else:
    save_tips()


@app.get("/")
def index():
    return render_template("index.html", tips=tips)


@app.post("/tips")
def add_tip():

    text = request.form.get("text").strip()

    if not text:
        return redirect("/")
    
    tips.append({"id": str(uuid4()), "text": text, "likes": 0})
    save_tips()
    return redirect("/")


@app.post("/tips/<tip_id>/like")
def like_tip(tip_id):
    for tip in tips:
        if tip["id"] == tip_id:
            tip["likes"] += 1
    save_tips()
    return redirect("/")


@app.post("/tips/<tip_id>/dislike")
def dislike_tip(tip_id):
    for tip in tips:
        if tip["id"] == tip_id:
            tip["likes"] += -1
    save_tips()
    return redirect("/")


@app.post("/tips/<tip_id>/delete")
def delete_tip(tip_id):
    for i, tip in enumerate(tips):
        if tip_id == tip["id"]:
            tips.pop(i)
            break
    save_tips()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=3000)
