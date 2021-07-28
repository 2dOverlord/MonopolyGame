

window.onload=function (){
    var sellformlink = document.getElementById('popup-link')

    var sellformdiv = document.getElementById('popup')

    sellformlink.onclick = function () {
    sellformdiv.setAttribute('visibility', 'visible');
    return false;
}

}

