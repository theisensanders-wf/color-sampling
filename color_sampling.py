from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    primary = '#' + request.args.get('primary', 'FFFFFF')
    secondary = '#' + request.args.get('secondary', '000000')

    print primary
    return render_template('index.html', primary=primary, secondary=secondary)

@app.route('/parakee')
def parakee():
    colors = [
        ['334D5C', 'DF5A49'],
        ['e67e22', '16828c']
    ]
    return render_template('parakee.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
