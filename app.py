from flask import fask, request, jsonify, render_template

app = Flask(__name__)

timetable = []

@app.route('/')
def index():
    return render_template('timetable.html')

@app.route('/api/timetable', methods=['GET', 'POST'])
def manage_timetable():
    if request.method == 'POST':
        data = request.json
        # Simple AI-like validation could be added here
        timetable.append(data)
        return jsonify({"message": "Timetable entry added", "entry": data}), 201
    else:  # GET
        return jsonify(timetable)

if __name__ == '__main__':
    app.run(debug=True)