from flask import Flask
import controllers

app = Flask(__name__, template_folder='templates')

# Example how to add a blueprint to hierarchy
# app.register_blueprint(controllers.login)

app.register_blueprint(controllers.index)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
