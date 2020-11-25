from flask import Flask, render_template 
app = Flask(__name__)   
@app.route('/play')          
def lets_play():
    return render_template('index.html') 
@app.route('/play/<int:times>')          
def play_time(times):
    return render_template('index2.html',t=times) 
@app.route('/play/<int:times>/<color>')          
def play_color(times, color):
    return render_template('index3.html',t=times, col=color) 
if __name__=="__main__":  
    app.run(debug=True)   
