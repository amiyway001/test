var canvas = document.getElementById('canvas');
var ctx = canvas.getContext('2d');

ctx.strokeStyle = 'gray';
ctx.lineWidth = 2;

function addLinkToCanvas(link) {
    ctx.beginPath();
    ctx.moveTo(100, 100);
    ctx.lineTo(200, 200);
    ctx.stroke();
    ctx.font = '24px Arial';
    ctx.fillText(link, 100, 100);
}

// TO DO: Implement canvas integration with Flask app