# How I did it was:

```
render_template function

for larger HTML files or for separating HTML from your Python code, it's recommended to use Flask's template rendering capabilities with the render_template function. This allows you to keep your HTML in separate files in a templates directory. 
```



# The whole Copilot explanation to this:

To use the `render_template` function in Flask, you need to do the following:

1. Import `render_template` from the flask module.
2. Create a `templates` directory in the same directory as your script.
3. Inside the `templates` directory, create an HTML file (for example, `index.html`).
4. In your route function, instead of returning a string of HTML, call `render_template` with the name of your HTML file as a string.

Here's how you can modify your code:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
```

And here's a simple `index.html` file you can put in your `templates` directory:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Flask Website</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>Welcome to my first Flask website!</p>
</body>
</html>
```

Now, when you navigate to the root URL of your Flask application, Flask will render the `index.html` template and return it as the response.