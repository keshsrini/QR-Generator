from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['url']
        img = qrcode.make(data)
        buffered = BytesIO()
        img.save(buffered)
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return render_template('index.html', img_data=img_str)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)