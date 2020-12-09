from flask import Flask, render_template

#import a class called blueprint

from flask import Blueprint

tasks_blueprint = Blueprint("tasks", __name__)

@tasks_blueprint.route('/tasks')
def tasks():
    return render_template("tasks/index.html")