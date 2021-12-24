
from flask import *
import json, time

app = Flask(__name__)
def home_page():
  data_set = {'timestamp': time.time()}
  json_dump = json.dumps(data_set)
  return json_dump


