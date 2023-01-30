from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
Bootstrap4(app)


@app.route("/")
def index():

    return "<a href='/posts'>Posts</a>"


@app.route("/redirect")
def redirect2():

    return redirect(url_for("response"))


@app.route("/response")
def response():
    headers = {
        "content-Type": "text/html"
    }
    return render_template("response.html")


@app.route("/posts")
@app.route("/posts/<int:id>")
def posts(id):
    titulo = request.args.get("titulo")

    data = dict(
        path=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        titulo=titulo,
        id=id if id else 0
    )

    return data


"""  o debug serve tanto para depurar nosso código, como tbm pra reiniciar nosso servidor automatico
 """
if __name__ == "__main__":
    app.run(debug=True)
