from main import Run
from flask_api import app

if __name__=='__main__':
    s=Run()
    s.run_start()
    app.run()