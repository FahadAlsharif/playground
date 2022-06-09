from flask import Flask , render_template

app = Flask(__name__)  
# @app.route("/play")
# def hello():
#     print("whatever")
#     return render_template("index.html")

# @app.route("/play")
# def help():
#     return render_template('index.html', num=3)
@app.route("/play")
@app.route("/play/<num>")
@app.route("/play/<color>")
@app.route("/play/<num>/<color>")
def boxnum(num=3, color = "red"):
    # print(num)
    return render_template('index.html', num=int(num),Bcolor = color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)
    