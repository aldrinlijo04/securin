from flask import Flask, request, jsonify, render_template
from models import db, Securin
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
import pymysql

pymysql.install_as_MySQLdb() 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)


@app.route("/api/cpes")
def get_cpes():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    query = Securin.query
    products = query.paginate(page=page, per_page=limit, error_out=False).items
    return jsonify({"products": [p.to_dict() for p in products]})


@app.route("/api/search")
def search_cpes():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    search = request.args.get("search", "").strip()
    deprecation = request.args.get("deprecation", "").strip()

    query = Securin.query
    if search:
        query = query.filter(Securin.cpe_title.ilike(f"%{search}%"))
    if deprecation:
        query = query.filter(Securin.cpe_23_deprecation_date.like(f"{deprecation}%"))

    products = query.paginate(page=page, per_page=limit, error_out=False).items
    return jsonify({"products": [p.to_dict() for p in products]})


@app.route("/")
def frontend():
    return render_template(r"frontend.html")


if __name__ == '__main__':
    app.run(debug=True)