from flask import Flask, render_template 
app = Flask(__name__)   
@app.route('/')          
def Checkerboard88():
    return render_template('index.html') 
@app.route('/<int:Xtimes>')          
def Checkerboard84(Xtimes):
    return render_template('index2.html',x=Xtimes) 
@app.route('/<int:Xtimes>/<int:Ytimes>')          
def CheckerboardXX(Xtimes, Ytimes):
    return render_template('index3.html',x=Xtimes, y=Ytimes) 
if __name__=="__main__":  
    app.run(debug=True)   
