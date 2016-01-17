from flask import Flask


app = Flask(__name__)

from DRApp.dr_app.views import grab, store
