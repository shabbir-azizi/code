from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            return f"<h1>Hello, {name}!</h1>"
        return "<h1>Please enter your name.</h1>"
    return '''
        <form method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name">
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)










    