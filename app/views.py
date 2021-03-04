from flask import render_template, abort, jsonify, request, redirect, url_for
from app.model import db, save_db
from app import app


@app.route("/")
def welcome():
    #return "Hello there"
    return render_template(
        "welcome.html",
        message="This data was sent from the view to the template",
        projects=db
    )


@app.route("/project/<int:index>")
def project_view(index):
    try:
        project = db[index]
        return render_template(
                                "project.html",
                                project=project,
                                index=index,
                                max_index=len(db)-1
                               )
    except IndexError:
        abort(404)


@app.route('/add_project', methods=["GET", "POST"])
def add_project():
    if request.method == "POST":
        # form has been submitted, process data
        card = {"language": request.form['language'],
                "description": request.form['description']}
        db.append(card)
        save_db()
        return redirect(url_for('project_view', index=len(db)-1))
    else:
        return render_template("add_project.html")


@app.route('/remove_project/<int:index>', methods=["GET", "POST"])
def remove_project(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_project.html", card=db[index])
    except IndexError:
        abort(404)


@app.route("/api/project/")
def api_project_list():
    return jsonify(db)


@app.route('/api/project/<int:index>')
def api_project_detail(index):
    try:
        return db[index]
    except IndexError:
        abort(404)
