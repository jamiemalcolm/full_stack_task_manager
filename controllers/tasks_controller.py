from flask import Flask, render_template
from repositories import task_repository

#import a class called blueprint

from flask import Blueprint

tasks_blueprint = Blueprint("tasks", __name__)
# this is our index and will get all of our tasks 
@tasks_blueprint.route('/tasks')
def tasks():
    # get all the tasks from the DB using the repository functions 
    tasks = task_repository.select_all()
    return render_template("tasks/index.html", all_tasks = tasks)


# NEW 
# GET '/tasks/new'
# return to the browser a new html form 
@tasks_blueprint.route('/tasks/new')
def new_task():
    return render_template("tasks/new.html")




# CREATE 
# POST '/tasks'

# SHOW 
# GET '/tasks/<id>'

#EDIT 
#GET '/tasks/<id>'

# UPDATE
#  POST'/tasks/<id>'

#DELETE
# POST '/tasks/<id>'