/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function re_position_rtl_resizeHandles() {
    /**
     * 
     * @type NodeList
     */

    // change positions of rtl resizeHandles
    var rtlNodes = document.getElementsByClassName("lang_rtl");
    for (var i = 0; i < rtlNodes.length; ++i) {
        var rtlResizeHandles = rtlNodes[i].getElementsByClassName("resizeHandle");
        for (var j = 0; j < rtlResizeHandles.length; ++j) {
            rtlResizeHandles[j].style.left = "1px";
            rtlResizeHandles[j].style.right = "";
        }
    }
}

window.onload = function () {
    drag_and_drop_init();
    re_position_rtl_resizeHandles();
    document.getElementById("alerter").innerHTML = "ready";
};
