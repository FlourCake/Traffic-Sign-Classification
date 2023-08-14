from project import App

if __name__ == '__main__':
    app = App('app', 'project/templates', 'project/static')
    app = app.create_app()
    app.run(host='localhost', port=5000, debug=True)