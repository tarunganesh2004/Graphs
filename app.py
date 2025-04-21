from flask import Flask, render_template_string

app = Flask(__name__)




@app.route("/")
def show_code():
    # Read content from the Python and Java files
    with open("graphRepresentation.py", "r") as f:
        graph_representation_python = f.read()
    with open("graphRepresentation.java", "r") as f:
        graph_representation_java = f.read()
    # with open("bfs.py", "r") as f:
    #     bfs_python = f.read()
    # with open("dfs.py", "r") as f:
    #     dfs_python = f.read()
    with open("bfsGraph.java", "r") as f:
        bfs_java = f.read()
    # with open("dfs.java", "r") as f:
    #     dfs_java = f.read()

    # Render the HTML template
    return render_template_string(
        """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Graph Algorithms</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism.css" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-java.min.js"></script>
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
                margin-bottom: 20px;
            }
            code {
                font-family: Consolas, "Courier New", monospace;
            }
            h2 {
                margin-top: 40px;
            }
        </style>
    </head>
    <body>
        <h1>Graph Algorithms Viewer</h1>
        
        <h2>1. Graph Representation</h2>
        <p>Below is the implementation of graph representation in Python and Java:</p>
        <h3>Python Implementation:</h3>
        <pre><code class="language-python">{{ graph_representation_python }}</code></pre>
        <h3>Java Implementation:</h3>
        <pre><code class="language-java">{{ graph_representation_java }}</code></pre>
        
        <h2>2. Breadth-First Search (BFS)</h2>
        <p>Breadth-First Search (BFS) explores a graph layer by layer starting from a source node. Here are the Python and Java implementations:</p>
        <h3>Python Implementation:</h3>
        <pre><code class="language-python">{{ bfs_python }}</code></pre>
        <h3>Java Implementation:</h3>
        <pre><code class="language-java">{{ bfs_java }}</code></pre>
        
        <h2>3. Depth-First Search (DFS)</h2>
        <p>Depth-First Search (DFS) explores as far as possible along a branch before backtracking. Here are the Python and Java implementations:</p>
        <h3>Python Implementation:</h3>
        <pre><code class="language-python">{{ dfs_python }}</code></pre>
        <h3>Java Implementation:</h3>
        <pre><code class="language-java">{{ dfs_java }}</code></pre>
    </body>
    </html>
    """,
        graph_representation_python=graph_representation_python,
        graph_representation_java=graph_representation_java,
        # bfs_python=bfs_python,
        # dfs_python=dfs_python,
        bfs_java=bfs_java,
        # dfs_java=dfs_java,
    )


if __name__ == "__main__":
    app.run(debug=True)
