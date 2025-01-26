from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def show_code():
    with open("graphRepresentation.py", "r") as f:
        code = f.read()
    return render_template_string(
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Python Code Viewer</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.css" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
            }
            pre {
                background-color: #f4f4f4;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                overflow-x: auto;
            }
            code {
                font-family: Consolas, "Courier New", monospace;
                color: #333;
            }
        </style>
    </head>
    <body>
        <h1>This page contains all graph algorithms implemented both in Python and Java</h1>
        <h2>Graph Representation In Different Ways</h2>
        <p>Below is the Python code from the file <strong>graphRepresentation.py</strong>:</p>
        <pre><code class="language-python">{{ code }}</code></pre>
    </body>
    </html>
    """,
        code=code,
    )


if __name__ == "__main__":
    app.run(debug=True)
