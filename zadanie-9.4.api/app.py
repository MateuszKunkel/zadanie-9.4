from flask import Flask, jsonify, abort, make_response, request
from api_records import api_records

app = Flask(__name__)
app.config["SECRET_KEY"] = "blablabla"


@app.route("/api/v1/books/", methods=["GET"])
def records_list_api_v1():
    return jsonify(api_records.all())


@app.route("/api/v1/books/", methods=["POST"])
def create_record():
    if not request.json:
        abort(400)
    if any(
        [
            not "recordauto" in request.json,
            not "recordname" in request.json,
            not "recordtext" in request.json,
            not "recordstar" in request.json,
        ]
    ):
        abort(400)

    record = {"id": api_records.all()[-1]["id"] + 1}
    record.update(request.json)
    api_records.create(record)
    return jsonify({"book": record}), 201


@app.route("/api/v1/books/<int:record_id>", methods=["GET"])
def get_record(record_id):
    record = api_records.get(record_id)
    if not record:
        abort(404)
    return jsonify({"book": record})


@app.route("/api/v1/books/<int:record_id>", methods=["PUT"])
def update_record(record_id):
    record = api_records.get(record_id)
    if not record:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any(
        [
            "recordauto" in data and not isinstance(data.get("recordauto"), str),
            "recordname" in data and not isinstance(data.get("recordname"), str),
            "recordtext" in data and not isinstance(data.get("recordtext"), str),
            "recordstar" in data and not isinstance(data.get("recordstar"), int),
        ]
    ):
        abort(400)

    record = {"id": record["id"]}
    record.update(request.json)
    api_records.update(record_id, record)
    return jsonify({"book": record})


@app.route("/api/v1/books/<int:record_id>", methods=["DELETE"])
def delete_record(record_id):
    result = api_records.delete(record_id)
    if not result:
        abort(404)
    return jsonify({"Deletion result": result})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found", "status_code": 404}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request", "status_code": 400}), 400)


if __name__ == "__main__":
    app.run(debug=True)
