from flask import Flask, render_template, request
import qrcode

app = Flask(__name__) # main entry point

@app.route("/", methods=["GET", "POST"]) # /(home-page)
def home():
    qr_image = None

    if request.method == "POST":
        link = request.form["link"]

        img = qrcode.make(link)
        img.save("static/qr.png")

        qr_image = "qr.png"

    return render_template("index.html", qr_image=qr_image)

if __name__ == "__main__":
    app.run()