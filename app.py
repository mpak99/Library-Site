import flask
from books_model import Book


app=flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/newbook",methods=["POST", "GET"])
def newbook():
    if flask.request.method =="POST":
        book=dict(flask.request.form)
        try:
            book['price']=float(book['price'])
            book['pages']=int(book['pages'])
            Book(book['ISBN'],book['title'],book['author'],book['price'],book['pages'])
        except:
            return flask.render_template('error.html')
        return flask.render_template('/index.html')
    return flask.render_template("/newbook.html")

@app.route('/bookslist')
def booklist():
    return flask.render_template('bookslist.html' ,allbooks=list(Book.list()))

@app.route('/deletebook' ,methods=['POST' , 'GET'])
def deletebook():
    if flask.request.method == 'POST' :
        book=dict(flask.request.form)
        print(book)
        try:
            Book.delete(int(book['ISBN']))
        except:
            return flask.render_template('error.html')
        return flask.render_template('index.html')
    return flask.render_template('deletebook.html')


if __name__ == '__main__' :
    app.run(debug=True)
