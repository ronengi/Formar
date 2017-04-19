
function dragged(ev) {
    // console.log(ev.target);
    ev.target.style.backgroundColor = "lightblue";
    // document.getElementById("alerter").innerHTML = ev.target.style.left;
    console.log(ev.target.style.left);
    ev.target.style.left = "0px";

}

