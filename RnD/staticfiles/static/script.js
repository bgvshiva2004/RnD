var side_bar = document.querySelector(".side-bar");
var ham = document.querySelector(".ham p");
var closes = document.getElementById("close");

ham.addEventListener("click", ()=>{
    side_bar.classList.toggle("show-side");
});

closes.addEventListener("click", ()=>{
    side_bar.classList.toggle("show-side");
});

var nav1 = document.querySelector(".navbar1");
var val;
window.onscroll = function(){
    if(document.documentElement.scrollTop > 20){
        nav1.classList.add("sticky");
    }
    else{
        nav1.classList.remove("sticky");
    }
}

console.log("script.js")