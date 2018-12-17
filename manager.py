# manage.py
from flask_script import Manager, Server
from cloud_dashboard_end import app as flask_app

manage = Manager(flask_app)
manage.add_command('runserver', Server(host='0.0.0.0', port=5082, use_debugger=True))

if __name__ == '__main__':
    manage.run()
