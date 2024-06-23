from flask import Flask, request, jsonify
import darkweb
import surfaceweb

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    nav = request.args.get('nav')

    if nav == 'darkweb':
        results = darkweb.search_darkweb(query)
    elif nav == 'surfaceweb':
        results = surfaceweb.search_surfaceweb(query)
    else:
        return jsonify({'error': 'Invalid navigation'}), 400

    return jsonify({'results': results})

@app.route('/add_link', methods=['POST'])
def add_link():
    link = request.form['link']
    # Add link to canvas
    # TO DO: Implement canvas integration
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)