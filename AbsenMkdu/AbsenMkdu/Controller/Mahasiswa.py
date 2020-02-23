from datetime import datetime
from flask import render_template
from AbsenMkdu import app
@app.route('/mhs')
def helloMhs():
        return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Hello '
    )

