import os
from waitress import serve
from microblog import app

serve(app,host="0.0.0.0",port=os.environ["PORT"])