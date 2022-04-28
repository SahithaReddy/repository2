from config import app
@app.get('/home')
def greetnow():
    return " any message"
@app.get('/sample')
def fun():
    return "random number"