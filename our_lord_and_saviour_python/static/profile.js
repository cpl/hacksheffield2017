// JavaScript source code
var colors = [ "#001f3f","#0074D9", "#7FDBFF", "#39CCCC", "#3D9970", "#2ECC40", "#01FF70", "#FFDC00", "#FF851B", "#FF4136", "#85144b", "#F012BE", "#B10DC9","#111111","#AAAAAA", "#DDDDDD"];
/*function load(){
    var randomColor = colors[Math.floor(Math.random() * colors.length)];
    var stringFinalColor = hex_to_RGB(randomColor);
    
    $(".focus").css("background-color", randomColor);
}*/
function hex_to_RGB(hex) {
    var m = hex.match(/^#?([\da-f]{2})([\da-f]{2})([\da-f]{2})$/i);
    return {
        r: parseInt(m[1], 16),
        g: parseInt(m[2], 16),
        b: parseInt(m[3], 16)
    };
}