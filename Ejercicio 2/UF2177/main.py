from flask import Flask
from connector import ConnectorDatabase
from repository import Repository
from controller import Routes
if __name__ == '__main__':
    app = Flask(__name__)
    connector = ConnectorDatabase("localhost", "root", "", "testalex", "3306")
    repository = Repository(connector)
    routes = Routes(app, repository)






