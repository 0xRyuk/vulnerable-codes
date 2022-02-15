from flask import Flask, render_template_string, request


app = Flask(__name__)


def filter(user_input):
    user_input = (
        user_input.replace("script", "")
        .replace("alert", "")
        .replace("prompt", "")
        .replace("confirm", "")
        .replace(">", "&gt;")
        .replace("\"", "\"\\")
    )
    if (
        "script" not in user_input
        and "alert" not in user_input
        and "prompt" not in user_input
        and "confirm" not in user_input
    ):
        return user_input
    return filter(user_input)


@app.route("/")
def index():
    name = request.args.get("name")
    if not name:
        name = "0xRyuk"

    page = """

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Xss!</title>
</head>
<body>
    <h1>Xss is fun!</h1>
    Hello, <b><span id="name">{}</span></b>
</body>

</html>
""".format(
        filter(name)
    )
    return render_template_string(page)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80, debug=True)
