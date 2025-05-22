# vamos a hacer una interfaz que diiga hola munfo 
# 07/04/2025

from flask import Flask 
app=Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Holiwis '

if __name__ =='__main__':
    app.run(debug=True)