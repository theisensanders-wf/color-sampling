from flask import Flask, render_template, request
import random

app = Flask(__name__)

colors = [
    ['4A96AD', '7D1935'],
    ['000000', '75B74B'],
    ['334D5C', 'DF5A49'],
    ['e67e22', '16828c'],
    ['A8CD1B', '005A31'],
    ['2ECC71', 'FF6666'],
    ['046380', 'E6E2AF'],
    ['E44424', '67BCDB'],
    ['B71427', 'FFE658']
]

@app.route('/')
def index():
    color = random.choice(colors)
    primary = request.args.get('primary', color[0])
    secondary = request.args.get('secondary', color[1])
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
    bird_colors = colors[:]
    return render_template('parakee.html', colors=bird_colors)


if __name__ == '__main__':
    app.run(debug=True)
