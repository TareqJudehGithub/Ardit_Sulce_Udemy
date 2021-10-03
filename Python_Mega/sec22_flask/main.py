from flask import Flask, app


app=Flask(__name__)

# homepage
@app.route("/")
def homepage():
  return "Website content"

# about page
@app.route("/about")
def about_page():
  return "About page"

if __name__ == "__main__":
  app.run(debug=True)