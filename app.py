from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Simple Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
        }
        header {
            background: #2c3e50;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }
        nav {
            background: #34495e;
            padding: 0.5rem;
            text-align: center;
        }
        nav a {
            color: #fff;
            margin: 0 15px;
            text-decoration: none;
        }
        main {
            max-width: 800px;
            margin: 20px auto;
            padding: 0 20px;
        }
        footer {
            background: #2c3e50;
            color: #fff;
            text-align: center;
            padding: 1rem 0;
            margin-top: 40px;
        }
    </style>
</head>
<body>

    <header>
        <h1>Welcome to My Website</h1>
        <p>A clean and simple HTML5 webpage</p>
    </header>

    <nav>
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#contact">Contact</a>
    </nav>

    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>Hello! This is a simple website built using standard HTML and a bit of internal CSS for layout and colors.</p>
        </section>

        <section id="services">
            <h2>What I Do</h2>
            <ul>
                <li>Web Design</li>
                <li>Content Writing</li>
                <li>Project Consulting</li>
            </ul>
        </section>

        <section id="contact">
            <h2>Contact</h2>
            <p>Feel free to reach out via email at <a href="mailto:hello@example.com">hello@example.com</a>.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 My Simple Website. All rights reserved.</p>
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)
