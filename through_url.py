#.........program through url..........

from flask import Flask , request , jsonify
app = Flask(__name__)

@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")     # get the data by the url
    mobil = request.args.get("mobil")
    email = request.args.get("email")

    return "this is my first string {} {} {} ".format(get_name , mobil,email)

if __name__ == "__main__":
    app.run(port= 5008)