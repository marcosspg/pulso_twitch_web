var startBTN = document.getElementsByClassName("startbtn")[0];
var btnDashed = false;
setInterval(() => {
    if(btnDashed){
        startBTN.style.border = "dotted"
    }else{
        startBTN.style.border = "dashed"
    }
    btnDashed = !btnDashed;
}, 400);