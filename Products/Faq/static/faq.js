/* ! FAQ Scripts */

displayAll = 0;
items = 0;

function toggle(id) {
    el = document.getElementById("faq_" + id);
    icon = document.getElementById("icon_" + id);

    if (el) {
        if (el.style.display == "block"){
            el.style.display = "none";
            icon.src = "treeCollapsed.gif";
        } else {
            el.style.display = "block";
            icon.src = "treeExpanded.gif";
        }
    }
}

function toggle_all(items) {
    for(var i = 1; i <= items; i++) {
        el = document.getElementById("faq_" + i);
        icon = document.getElementById("icon_" + i);
        if (el) {
            if (displayAll) {
                el.style.display = "none";
                icon.src = "treeCollapsed.gif";
            } else {
                el.style.display = "block";
                icon.src = "treeExpanded.gif";
                }
            }
        }
        displayAll = (displayAll ? 0 : 1);
}

function overLinkStyle(link_id) {
        document.getElementById(link_id).style.cursor = 'pointer';
}

function outLinkStyle(link_id) {
    document.getElementById(link_id).style.cursor = 'default';
}
