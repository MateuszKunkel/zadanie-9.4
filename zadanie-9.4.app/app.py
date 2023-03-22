from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
)
from forms import RecordsForm
from models import records

app = Flask(__name__)
app.config["SECRET_KEY"] = "bardzotajnyklucz"


# ___________/records/___________________GET/POST


@app.route("/records/", methods=["GET"])
def get_records():
    form = RecordsForm()
    error = ""
    return render_template(
        "records.html", form=form, records=records.all(), error=error
    )


@app.route("/records/", methods=["POST"])
def post_records():
    form = RecordsForm()

    if form.validate_on_submit():
        record = {
            "id": records.all()[-1]["id"] + 1,
            "recordauto": form.data["recordauto"],
            "recordname": form.data["recordname"],
            "recordtext": form.data["recordtext"],
            "recordstar": form.data["recordstar"],
        }
        records.create(record)
    return redirect(url_for("get_records"))


# ___________/records/<id>_______________GET/POST


@app.route("/records/<int:record_id>/", methods=["GET"])
def get_records_id(record_id):
    record = records.get(record_id)
    form = RecordsForm(data=record)
    return render_template("record.html", form=form, record_id=record_id)


@app.route("/records/<int:record_id>/", methods=["POST"])
def put_records_id(record_id):
    form = RecordsForm()
    record = records.get(record_id)

    record = {
        "id": record["id"],
        "recordauto": form.data.get("recordauto", record["recordauto"]),
        "recordname": form.data.get("recordname", record["recordname"]),
        "recordtext": form.data.get("recordtext", record["recordtext"]),
        "recordstar": form.data.get("recordstar", record["recordstar"]),
    }

    records.update(record_id, record)
    return redirect(url_for("get_records"))


# ___________/records/<id>/read__________GET


@app.route("/records/<int:record_id>/read/", methods=["GET"])
def get_records_id_watch(record_id):
    record = records.get(record_id)
    form = RecordsForm(data=record)
    return render_template("recordwatcher.html", form=form, record=record)


# ____________main_______________________


if __name__ == "__main__":
    app.run(debug=True)
