var dark_theme = 'css/dark.css';
var light_theme = 'css/light.css';

function toggle_theme(){
    var current_theme = document.getElementById('style').getAttribute('href');
    if (current_theme==dark_theme){
        document.getElementById('style').setAttribute('href', light_theme);
    } else if (current_theme==light_theme){
        document.getElementById('style').setAttribute('href', dark_theme);
    }
}

function scroll_check(){
    var top_scroll = window.pageYOffset;

    /*if (top_scroll > (128)){
        console.log("maior");
    }*/

    requestAnimationFrame(scroll_check);
}
scroll_check();
