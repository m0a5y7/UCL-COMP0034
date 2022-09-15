from flask_app import create_app, app

app = create_app(app)


if __name__ == '__main__':
    app.run(debug=True)