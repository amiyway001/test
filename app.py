from flask import Flask, request, jsonify,render_template

import darkweb
import surfaceweb

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    
    nav = request.form['nav']
    results = []
    if nav == 'darkweb':
        results = darkweb.search_darkweb(query)
    
    elif nav == 'surfaceweb':
        results = surfaceweb.search_surfaceweb(query)
    
    print(results)
    return render_template('index.html', results=results, query=query, nav=nav)


@app.route('/add_link', methods=['POST'])
def add_link():
    link = request.form['link']
    # Add link to canvas
    # TO DO: Implement canvas integration
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)