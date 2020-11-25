from flask import Flask, render_template, request, redirect, session
import random

def compare(userinput, computerchoice, userscore, computerscore, results_msg, whoWin, lost, nowin):
    if userinput == "rock" and computerchoice == "scissors":
        results_msg="You choose "+userinput+" and the computer choose "+computerchoice
        whoWin="You won this round!"
        userscore += 1
    elif userinput == "rock" and computerchoice == "paper":
        results_msg="You choose "+userinput+" and the computer choose "+computerchoice
        lost="You lost this round :("
        computerscore += 1
    if userinput == "paper" and computerchoice == "rock":
        results_msg="You choose "+userinput+" and the computer choose "+computerchoice
        whoWin="You won this round!"
        userscore += 1
    elif userinput == "paper" and computerchoice == "scissors":
        results_msg="You choose "+userinput+" and the computer choose "+computerchoice
        lost="You lost this round :("
        computerscore += 1
    if userinput == "scissors" and computerchoice == "paper":
        results_msg="You choose "+userinput+" and the computer choose "+computerchoice
        whoWin="You won this round!"
        userscore += 1
    elif userinput == "scissors" and computerchoice == "rock":
        results_msg="You choose "+userinput+" and the computer choose "+computerchoice
        lost="You lost this round :("
        computerscore += 1
    if userinput == computerchoice:
        results_msg="You choose "+userinput+" and the computer choose "+computerchoice
        nowin="No winner for this round.."
    return userscore, computerscore, results_msg, whoWin, lost, nowin

app = Flask(__name__) 
app.secret_key = 'keep it secret, keep it safe'   
@app.route('/')          
def hello_world():
    if 'count' not in session:
        session['count']=0
        session['computerscore']=0
        session['userscore']=0
    else:
        session['count']+=1
    return render_template('index.html')

@app.route('/winner', methods=['POST'])          
def winner():
    session['player'] =request.form['choice']
    session['PC'] = random.choice(["rock","paper","scissors"])
    session['results_msg']=''
    session['whoWin']=''
    session['lost']=''
    session['nowin']=''
    session['userscore'], session['computerscore'], session['results_msg'], session['whoWin'], session['lost'], session['nowin']= compare(session['player'], session['PC'], session['userscore'], session['computerscore'], session['results_msg'], session['whoWin'], session['lost'], session['nowin'])
    return redirect('/show')

@app.route('/show', methods=['GET'])
def show_results():

    playerImg="static/"+session['player']+".png"
    PCImg="static/"+session['PC']+".png"
    return render_template('index1.html', pc=PCImg, p=playerImg, Uscore=session['userscore'], Cscore=session['computerscore'], msg=session['results_msg'], win=session['whoWin'], lost=session['lost'], nowin=session['nowin'])

@app.route('/reset')
def reset():
	session['userscore']=session['computerscore']=session['count'] = 0
	return redirect ('/')
if __name__=="__main__":      
    app.run(debug=True)  