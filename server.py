import os
from package import app

# Localhost setup - http://localhost:5000/
if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.debug = True
        app.run(host='localhost', port=port)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



@app.route('/Camera')
def Camera():
    from python_files import faceLogin
