from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__) 
    
@app.route("/")
def render_main():
   return render_template("home.html")
   
@app.route("/page1")
def render_p1():
    htow={"Ben Carson":"Wayne","Bernie Sanders":"Kings","Carly Fiorina":"Travis","Chris Christie":"Essex","Donald Trump":"Queens",
    "Hillary Clinton":"Cook","Jeb Bush":"Midland","John Kasich":"Allegheny","Marco Rubio":"Miami-Dade","Martin O'Malley":"D.C.",
    "Mike Huckabee":"Hempstead","Rand Paul":"Allegheny","Rick Santorum":"Frederick","Ted Cruz":"Harris"}
   {%hoco%}=print(htow)
   for candidatein htow:
    {%can%}=print(candidate)
   return render_template("page1.html",{%hoco%}=print(htow),{%can%}=print(candidate))
   
@app.route("/page2")
def render_p2():
   return render_template("page2.html")
   
@app.route("/page3")
def render_p3():
   return render_template("page3.html")
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
