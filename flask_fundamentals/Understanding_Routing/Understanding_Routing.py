from flask import Flask  
app = Flask(__name__)   
@app.route('/')          
def hello_world():
    return 'Hello World!' 
@app.route('/dojo')          
def dojo_func():
    return 'Dojo!'
@app.route('/say/<name>')
def User_name(name):
    return "Hi "+name.capitalize()+"!"
@app.route('/repeat/<int:times>/<string:something>')
def repeat_somthing(something, times):
    return f"{something} "*times
@app.errorhandler(404)
def errorM(e):
    return "Error: Enter valid URL"
if __name__=="__main__":  
    app.run(debug=True)   
