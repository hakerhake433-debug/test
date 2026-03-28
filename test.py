import requests
import threading
import time
from flask import Flask, request, render_template_string

DOMAIN = "alphacourse"
TOKEN = "81b840dc-2b96-4166-a6ad-d9d90e792e07"

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Login Test</title>
</head>
<body style="font-family:Arial;text-align:center;margin-top:100px">

<h2>Login Page</h2>

<form method="POST">
<input type="text" name="username" placeholder="username" required><br><br>
<input type="password" name="password" placeholder="password" required><br><br>
<button type="submit">Login</button>
</form>

<p>{{message}}</p>

</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def login():
    message = ""
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        if user == "admin" and pw == "1234":
            message = "Login successful"
        else:
            message = "Wrong login"

    return render_template_string(html, message=message)


def update_duckdns():
    while True:
        try:
            url = f"https://www.duckdns.org/update?domains={DOMAIN}&token={TOKEN}&ip="
            r = requests.get(url)
            print("DuckDNS update:", r.text)
        except Exception as e:
            print("Error:", e)

        time.sleep(60)


threading.Thread(target=update_duckdns, daemon=True).start()

app.run(host="0.0.0.0", port=5000)