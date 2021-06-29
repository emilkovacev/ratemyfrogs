function copyURL() {
    /* Get the text field */
    let copyText = document.getElementById("frog-url");

    /* Select the text field */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* For mobile devices */

    /* Copy the text inside the text field */
    document.execCommand("copy");
    button = document.getElementById("copy-button")
    button.value = "copied!"
    button.style.borderColor = "rgb(25, 190, 60)"
    copyText.style.borderColor = "rgb(25, 190, 60)"
    button.style.color = "rgb(25, 190, 60)"
    button.id = "copy-button-no-hover"
    button.onclick = ""
}

function enlarge() {
    
    let container = document.getElementById("fullscreen-image-container")
    if (container.style.display == "") {
        container.style.display = "flex"
        
    } else {
        container.style.display = ""
    }
}

function darkMode() {
    let body = document.body;
    let button = document.getElementById("dark-mode-button")
    let localStorage = window.localStorage
    let mode = localStorage.getItem("mode")
    if (mode === "") {
        localStorage.setItem("mode", "dark")
        button.innerHTML = "light mode"
    } else if (mode == "dark") {
        localStorage.setItem("mode", "")
        button.innerHTML = "dark mode"
    }
    body.classList.toggle("dark-mode")
}

function showRankings() {
    let button = document.getElementById("ranking-button")
    let title = document.getElementById("ranking-title")
    let rankings = document.getElementById("ranking-container")

    if (title.style.display === "" && rankings.style.display === "") {
        title.style.display = "block"
        rankings.style.display = "grid"
        button.innerHTML = "hide rankings"
        button.scrollIntoView({behavior: 'smooth'});
    }
    else {
        title.style.display = ""
        rankings.style.display = ""
        button.innerHTML = "show rankings"
    }
}

function loadMode() {
    let body = document.body;
    let button = document.getElementById("dark-mode-button")
    let localStorage = window.localStorage
    let mode = localStorage.getItem("mode")
    if (mode == "dark") {
        document.body.classList.toggle("dark-mode")
        button.innerHTML = "light mode"
    } else {
        button.innerHTML = "dark mode"
    }
}

let localStorage = window.localStorage
let mode = localStorage.getItem("mode")
if (mode == null) {
    localStorage.setItem("mode", "")
} else if (mode === "dark") {
    document.body.classList.toggle("dark-mode")
}
