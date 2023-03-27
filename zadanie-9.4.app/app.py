from flask import Flask, render_template, redirect, url_for, request
from forms import RecordsForm
from models import records

app = Flask(__name__)
app.config["SECRET_KEY"] = "bardzotajnyklucz"


# ___________/records/___________________GET/POST


@app.route("/books/", methods=["GET", "POST"])
def get_records():
    form = RecordsForm()
    if request.method == "POST":
        if form.validate_on_submit():
            id = {"id": records.all()[-1]["id"] + 1}
            record = {**id,**form.data}
            records.create(record)
        return redirect(url_for("get_records"))
    error = ""
    return render_template(
        "records.html", form=form, records=records.all(), error=error
    )


# ___________/records/<id>_______________GET/POST


@app.route("/books/<int:record_id>/", methods=["GET", "POST"])
def get_records_id(record_id):
    record = records.get(record_id)
    form = RecordsForm(data=record)
    if request.method == "POST":
        if form.validate_on_submit():
            id = {"id": record["id"]}
            record = {**id,**form.data}
            records.update(record_id, record)
        return redirect(url_for("get_records"))
    return render_template("record.html", form=form, record_id=record_id)


# ___________/records/<id>/read__________GET


@app.route("/books/<int:record_id>/read/", methods=["GET"])
def get_records_id_watch(record_id):
    record = records.get(record_id)
    form = RecordsForm(data=record)
    return render_template("recordwatcher.html", form=form, record=record)


# ____________main_______________________


if __name__ == "__main__":
    app.run(debug=True)
