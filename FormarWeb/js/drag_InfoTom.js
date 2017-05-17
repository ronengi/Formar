/* 
 * InfoTom dragging
 */


// dragstart
function InfoTom_dragstart(event) {
    var dt = event.dataTransfer;
    var me = event.target;
    var myStyle = document.defaultView.getComputedStyle(me);
    var myLeft = parseInt(myStyle.getPropertyValue("left"), 10) - event.clientX;
    var myTop = parseInt(myStyle.getPropertyValue("top"), 10) - event.clientY;
    me.style.opacity = "0.9";
    // me.style.border = "1px dashed blue";
    dt.setData("text/plain", myLeft + "," + myTop);

    document.getElementById("alerter").innerHTML = "Dragging Information Node";
}


// drag
function InfoTom_drag(event) {
    // var dt = event.target;
    // dt.effectAllowed = "all";
    // dt.dropEffect = "move";
}


// dragover
function InfoTom_dragover(event) {
    var myData = event.dataTransfer.getData("text/plain").split(',');
    var me = document.getElementById("the_currently_dragged_thingy");
    var myLeft = parseInt(myData[0], 10);
    var myTop = parseInt(myData[1], 10);

    var dt = event.dataTransfer;
    dt.dropEffect = "move";
    var myData = dt.getData("text/plain").split(',');
    var myLeft = parseInt(myData[0], 10);
    var myTop = parseInt(myData[1], 10);
    me.style.left = myLeft + event.clientX + 'px';
    me.style.top = myTop + event.clientY + 'px';

}


// drop
function InfoTom_drop(event) {
    var me = document.getElementById("the_currently_dragged_thingy");
    me.id = "";
    me.style.opacity = "";
    document.getElementById("alerter").innerHTML = "ready";
}
