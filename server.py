from flask import Flask, render_template
from get_data import get_data
from get_logs import get_logs

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/datanode_warnings")
def datanode_warnings():
    return render_template('datanode_warnings.html', data=get_data('datanode_warnings'))


@app.route("/datanode_errors")
def datanode_errors():
    return render_template('datanode_errors.html', data=get_data('datanode_errors'))


@app.route("/namenode_warnings")
def namenode_warnings():
    return render_template('namenode_warnings.html', data=get_data('namenode_warnings'))


@app.route("/namenode_errors")
def namenode_error():
    return render_template('namenode_errors.html', data=get_data('namenode_errors'))


@app.route("/historyserver_warnings")
def historyserver_warnings():
    return render_template('historyserver_warnings.html', data=get_data('historyserver_warnings'))


@app.route("/historyserver_errors")
def historyserver_errors():
    return render_template('historyserver_errors.html', data=get_data('historyserver_errors'))


@app.route("/nodemanager_warnings")
def nodemanager_warnings():
    return render_template('nodemanager_warnings.html', data=get_data('nodemanager_warnings'))


@app.route("/nodemanager_errors")
def nodemanager_errors():
    return render_template('nodemanager_errors.html', data=get_data('nodemanager_errors'))


@app.route("/resourcemanager_warnings")
def resourcemanager_warnings():
    return render_template('resourcemanager_warnings.html', data=get_data('resourcemanager_warnings'))


@app.route("/resourcemanager_errors")
def resourcemanager_errors():
    return render_template('resourcemanager_errors.html', data=get_data('resourcemanager_errors'))


@app.route("/all_warnings")
def all_warnings():
    return render_template('all_warnings.html', data=get_data('all_warnings'))


@app.route("/all_errors")
def all_errors():
    return render_template('all_errors.html', data=get_data('all_errors'))


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/get_logs")
def getlogs():
    get_logs()
    return 0


if __name__ == '__main__':
    app.run()
