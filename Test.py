from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <head>
        <meta name="viewport"
              content="width=device-width, initial-scale=1">
      </head>
      <body>
        <h1>My Python Dashboard</h1>
        <p>My first Python website!</p>
        <form action="/run" method="post">
          <button type="submit">Run Python</button>
        </form>
      </body>
    </html>
    """

@app.route("/run", methods=["POST"])
def run_script():
    message = "Python script executed successfully!"
    return f"""
    <h1>Results</h1>
    <p>{message}</p>
    <a href="/">Go back</a>
    """
