# vamos a trabajar con flask 
# 29/04/2025

from flask import Flask 
app=Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'nopuedomas'

if __name__ =='__main__':
#     app.run(debug=True)
    app.run(host='0.0.0.0',port=5000)