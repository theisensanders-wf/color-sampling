from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    primary = request.args.get('primary', '333333')
    secondary = request.args.get('secondary', 'FFFFFF')
    reverse = request.args.get('reverse', 'false').lower() == 'true'

    primary_hex = '#' + primary
    secondary_hex = '#' + secondary

    if reverse:
        tmp = primary
        primary = secondary
        secondary = tmp

    return render_template('index.html', primary=primary, secondary=secondary,
                           primary_hex=primary_hex, secondary_hex=secondary_hex)

@app.route('/parakee')
def parakee():
    colors = [
        ['334D5C', 'DF5A49'],
        ['e67e22', '16828c'],
        ['A8CD1B', '005A31'],
        ['2ECC71', 'FF6666']
    ]
    return render_template('parakee.html', colors=colors)


if __name__ == '__main__':
    app.run(debug=True)
