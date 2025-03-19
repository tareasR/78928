from flask import Flask

app = Flask(__name__)

@app.route('/saludar')
def hola_mundo():
    return 'Hola Mundo!'

@app.route('/adios')
def adios_mundo():
    return 'Adios Mundo!'

@app.route('/hola')
def hola_html():
    return '<h1 style="color:red;">Hola!!</h1>'

@app.route('/json')
def json():
    return Response( '{"nombre":"john"}', mimetype='application/json' )

@app.route('/xml')
def xml():
    xml= '''<?xml version='1.0'?> 
    <persona>
    <nombre>john</nombre> 
    </persona>'''
    return Response(xml, mimetype='application/xml')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
