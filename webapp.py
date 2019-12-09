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
    host={"Ben Carson":"Michigan","Bernie Sanders":"New York","Carly Fiorina":"Texas","Chris Christie":"New Jersey","Donald Trump":"New York",
    "Hillary Clinton":"Illinois","Jeb Bush":"Texas","John Kasich":"Pennsylvania","Marco Rubio":"Florida","Martin O'Malley":"Virginia",
    "Mike Huckabee":"Arkansas","Rand Paul":"Pennsylvania","Rick Santorum":"Virginia","Ted Cruz":"Texas"}
    votes={}
    print(votes)
    for key in host:
        for data in dict:
            if data["Location"]["State"] == host[key]:
            
                #votes[key]+=data["Vote Data"][key]["Number of Votes"]
        #if data["Location"]["County"] in ["Location"]["State"]        
    return render_template("page1.html")
   
@app.route("/page2")
def render_p2():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    #for data in dict:
        #if data["Vote Data"]["Party"]=="democrat":
        #    return democrat
    return render_template("page2.html")#,dem=democrat,rep=republican)
   
@app.route("/page3")
def render_p3():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    return render_template("page3.html")
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
