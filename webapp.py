from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) 
    
@app.route("/")
def render_main():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    return render_template("home.html")
   
@app.route("/page2")
def render_p2():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    host={"Ben Carson":"Michigan","Bernie Sanders":"New York","Carly Fiorina":"Texas","Chris Christie":"New Jersey","Donald Trump":"New York",
    "Hillary Clinton":"Illinois","Jeb Bush":"Texas","John Kasich":"Pennsylvania","Marco Rubio":"Florida","Martin O'Malley":"Virginia",
    "Mike Huckabee":"Arkansas","Rand Paul":"Pennsylvania","Rick Santorum":"Virginia","Ted Cruz":"Texas"}
    votes={}
    graphpoint=""
    for key in host:
        for data in dict:
            if data["Location"]["State"] == host[key]:
                if key in votes:
                    votes[key]+=data["Vote Data"][key]["Number of Votes"]
                else:
                    votes[key]=data["Vote Data"][key]["Number of Votes"]
    for num in votes:
        if votes[num] == 0:
            graphpoint+= Markup( '{ y: ' + str(1000) + ', label: "' + str(num) + '",' + ' indexLabel: " ' + str(host[num]) + ' " },' )
            if str[num] == "Ted Cruz":
                graphpoint+= Markup( '{ y: ' + str(1000) + ', label: " Ted Cruz ", indexLabel: " Texas " }' )
        else:
            graphpoint+= Markup( '{ y: ' + str(votes[num]) + ', label: "' + str(num) + '",' + ' indexLabel: " ' + str(host[num]) + ' " },' )
    return render_template("page2.html",graphpoint = graphpoint)

@app.route("/page3")
def render_p3():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    #for data in dict:
        #if data["Vote Data"]["Party"]=="democrat":
        #    return democrat
    nopref=0
    for data in dict:
        nopref+= data["Vote Data"]["No Preference"]["Number of Votes"]
    uncommitted=0
    for data in dict:
        uncommitted+= data["Vote Data"]["Uncommitted"]["Number of Votes"]
    democrat=0
    for data in dict:
        for candidate in data["Vote Data"]:
            if data["Vote Data"][candidate]["Party"] == "Democrat":
                democrat+= data["Vote Data"][candidate]["Number of Votes"]
    republican=0
    for data in dict:
        for candidate in data["Vote Data"]:
            if data["Vote Data"][candidate]["Party"] == "Republican":
                republican+= data["Vote Data"][candidate]["Number of Votes"]
    return render_template("page3.html",no=nopref,un=uncommitted,dem=democrat,rep=republican)

   
@app.route("/page4")
def render_p4():
    with open('election.json') as electiondata:
        dict = json.load(electiondata)
    return render_template("page4.html")
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
