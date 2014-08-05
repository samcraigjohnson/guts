from guts import app

@app.route('/')
def index():
    return "Hello Julian"
