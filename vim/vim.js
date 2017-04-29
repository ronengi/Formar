window.onload = function() {


    // dragstart
    document.addEventListener("dragstart", function(event) {
        var dt = event.dataTransfer;

        var me = event.target;
        var myStyle = document.defaultView.getComputedStyle(me);

        var myLeft = parseInt(myStyle.getPropertyValue("left"), 10) - event.clientX;
        var myTop = parseInt(myStyle.getPropertyValue("top"), 10) - event.clientY;

        me.id = "the_dragged_thingy";
        me.style.backgroundColor = "lightblue";
        me.style.opacity="0.3";
        me.style.border = "1px dashed blue";

        dt.setData("text/plain", me.id + "," + myLeft + "," + myTop);
    });


    // drag
    document.addEventListener("drag", function(event) {
        event.preventDefault();
        var dt = event.target;
        dt.effectAllowed = "all";
        dt.dropEffect = "move";
    });


    // dragover
    document.addEventListener("dragover", function(event) {
        event.preventDefault();

        var dt = event.dataTransfer;
        var myData = dt.getData("text/plain").split(',');
        var myLeft = parseInt(myData[1], 10);
        var myTop = parseInt(myData[2], 10);

        document.getElementById("alerter").innerHTML = "(" + (myLeft + event.clientX) + ", " + (myTop + event.clientY) + ")";
    });


    /*
    // dragend
    document.addEventListener("dragend", function(event) {
       console.log("dragend");
    });
    */


    // drop
    document.addEventListener("drop", function(event) {
        event.preventDefault();

        var me = document.getElementById("the_dragged_thingy");
        var target = event.target;
        var dt = event.dataTransfer;

        dt.dropEffect = "move";
        var myData = dt.getData("text/plain").split(',');
        var myId = myData[0];
        var myLeft = parseInt(myData[1], 10);
        var myTop = parseInt(myData[2], 10);

        me.style.left = myLeft + event.clientX + 'px';
        me.style.top = myTop + event.clientY + 'px';

        me.id = "";
        me.style.backgroundColor = "";
        me.style.opacity = "";
        me.style.border = "";
    });


    document.getElementById("alerter").innerHTML = "ready";

}

