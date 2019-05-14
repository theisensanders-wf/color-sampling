const urlParams = new URLSearchParams(window.location.search);

const colors = [
    ['4A96AD', '7D1935'],
    ['000000', '7AC143'],
    ['334D5C', 'DF5A49'],
    ['e67e22', '16828c'],
    ['A8CD1B', '005A31'],
    ['2ECC71', 'FF6666'],
    ['046380', 'E6E2AF'],
    ['E44424', '67BCDB'],
    ['B71427', 'FFE658']
];

// Pick colors
var randomColor = colors[Math.floor(Math.random() * colors.length)];
var primaryColor = urlParams.get('primary') || randomColor[0];
var secondaryColor = urlParams.get('secondary') || randomColor[1];

// Set css variables
var root = document.documentElement;
root.style.setProperty('--primary-color', '#' + primaryColor);
root.style.setProperty('--secondary-color', '#' + secondaryColor);

// Set reverse color href
document.getElementById('reverse-colors').href = "?primary=" + secondaryColor + "&secondary=" + primaryColor;
