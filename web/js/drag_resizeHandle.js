/* 
 * resizeHandle dragging
 * 
 *  Information Node Dimentions Calculations During Resize:
 *      rtl
 *          width  =  width   + x1 - x2  (minWidth limitation)
 *          height =  height  - y1 + y2  (minHeight limitation)
 *          left   =  left    - x1 + x2
 *          top    =  top
 *      ltr
 *          width  =  width   - x1 + x2  (minWidth limitation)
 *          height =  height  - y1 + y2  (minHeight limitation)
 *          left   =  left
 *          top    =  top
 *      
 */


var minHeight = 90;
var minWidth = 150;


// dragstart
function resizeHandle_dragstart(event) {
    var dt = event.dataTransfer;
    var parent = event.target.parentNode;
    var parentStyle = document.defaultView.getComputedStyle(parent);
    var rtl = parent.classList.contains("lang_rtl"); 
    var parentLeft = parseInt(parentStyle.getPropertyValue("left"), 10);
    var parentTop = parseInt(parentStyle.getPropertyValue("top"), 10);
    var parentWidth = parseInt(parentStyle.getPropertyValue("width"), 10);
    var parentHeight = parseInt(parentStyle.getPropertyValue("height"), 10);
    parentHeight -= event.clientY;
    if (rtl) {
        parentWidth += event.clientX;
        parentHeight -+ event.clientY;
        parentLeft -= event.clientX;    
    }
    else {
        parentWidth -= event.clientX;
    }
    parent.style.opacity = "0.8";
    dt.setData("text/plain", parentLeft + "," + parentTop + "," + parentWidth + "," + parentHeight);

    document.getElementById("alerter").innerHTML = "Resizing Information Node";
}


// drag
function resizeHandle_drag(event) {
    // var dt = event.target;
    // dt.effectAllowed = "all";
    // dt.dropEffect = "move";

}


// dragover
function resizeHandle_dragover(event) {
    var myData = event.dataTransfer.getData("text/plain").split(',');
    var parent = document.getElementById("the_currently_dragged_thingy").parentNode;
    var rtl = parent.classList.contains("lang_rtl"); 
    var parentLeft = parseInt(myData[0], 10);
    var parentTop = parseInt(myData[1], 10);
    var parentWidth = parseInt(myData[2]);
    var parentHeight = parseInt(myData[3]);

    
    if (rtl) {
        var newWidth = parentWidth - event.clientX;
        var newHeight = parentHeight + event.clientY;
        var newLeft = parentLeft + event.clientX;
        if (newWidth > minWidth) {
            parent.style.left = newLeft + 'px';
            parent.style.width = newWidth + 'px';
        }
        if (newHeight > minHeight) {
            parent.style.height = newHeight + 'px';
        }
    }
    else {
        var newWidth = parentWidth + event.clientX;
        var newHeight = parentHeight + event.clientY;
        
        if (newWidth > minWidth) {
            parent.style.width = newWidth + 'px';
        }
        if (newHeight > minHeight) {
            parent.style.height = newHeight + 'px';
        }
    }
}


// drop (minWidth limitation)
function resizeHandle_drop(event) {
    var me = document.getElementById("the_currently_dragged_thingy");
    var parent = me.parentNode;
    me.id = "";
    parent.style.opacity = "";
    document.getElementById("alerter").innerHTML = "ready";
}
