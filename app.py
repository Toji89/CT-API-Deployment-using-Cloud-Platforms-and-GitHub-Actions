from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/db_name'
db = SQLAlchemy(app)

# Sum model
class Sum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Integer, nullable=False)
    num2 = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)

# Endpoint to retrieve sums filtered by result
@app.route('/sum/result/<int:filter_result>', methods=['GET'])
def get_sums_by_result(filter_result):
    sums = Sum.query.filter_by(result=filter_result).all()
    sums_list = [{'num1': sum.num1, 'num2': sum.num2, 'result': sum.result} for sum in sums]
    return jsonify(sums_list), 200

if __name__ == '__main__':
    app.run(debug=True)
