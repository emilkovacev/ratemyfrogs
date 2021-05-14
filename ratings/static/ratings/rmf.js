// Cookies

// setCookie and getCookie taken from https://www.w3schools.com/js/js_cookies.asp
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
        }
    }
    return "";
}

function setMode() {
    let currentMode = document.body.classList
    setCookie("mode", currentMode, 10);
}

function changeMode() {
    console.log("changing mode")
    let body = document.body;
    body.classList.toggle("dark-mode");
    setMode()
}

function getMode() {
    console.log("getting mode")
    let mode = getCookie("mode");

    if (mode == "dark-mode") {
        changeMode();
        // .checked doesn't seem to be working/updating checkbox element
        document.getElementsById("checkbox").checked = true;
    }
    else {
        console.log("to light-mode")
        document.body.classList.remove;
        // .checked doesn't seem to be working/updating checkbox element
        document.getElementsById("checkbox").checked = false;
    }
}

// AJAX Requests

