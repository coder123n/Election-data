from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) 
    
@app.route("/")
def render_main():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    return render_template("home.html")
   
@app.route("/page1")
def render_p1():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    htow={"Ben Carson":"Wayne","Bernie Sanders":"Kings","Carly Fiorina":"Travis","Chris Christie":"Essex","Donald Trump":"Queens",
    "Hillary Clinton":"Cook","Jeb Bush":"Midland","John Kasich":"Allegheny","Marco Rubio":"Miami-Dade","Martin O'Malley":"D.C.",
    "Mike Huckabee":"Hempstead","Rand Paul":"Allegheny","Rick Santorum":"Frederick","Ted Cruz":"Harris"}
    candidate=[]
    for key in htow:
        if key not in candidate:
            candidate.append(key)
    #for person in htow
    #    for data in dict
    #       if person 
    return render_template("page1.html",hoco=htow,can=candidate)
   
@app.route("/page2")
def render_p2():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    return render_template("page2.html",dem=democrat,rep=republican)
   
@app.route("/page3")
def render_p3():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    return render_template("page3.html")
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
