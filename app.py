from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = [
    {'id': 123, 'title': 'Harry Potter', 'author': 'J.K. Rowling', 'year': 2001},
    {'id': 1234, 'title': 'Dune', 'author': 'Frank Herbert', 'year': 2018},
    {'id': 12345, 'title': 'Dune 2', 'author': 'Frank Herbert', 'year': 2023}
]

@app.route('/')
def home():
    return render_template('index.html', books=books)
@app.route('/book_id/<int:book_id>')
def home1(book_id):
     if books['id'] == 123:
        return render_template('book_id.html', BOOK_ID=book_id)
     if books['id'] == 1234:
        return render_template('book_id.html', BOOK_ID=book_id)
     if books['id'] == 1235:
        return render_template('book_id.html', BOOK_ID=book_id)
@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    books.append({'title': title, 'author': author, 'year': year})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
