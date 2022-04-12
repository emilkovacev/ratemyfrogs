const copyURL = () => {
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

const enlarge = () => {
    
    let container = document.getElementById("fullscreen-image-container")
    if (container.style.display == "") {
        container.style.display = "flex"
        
    } else {
        container.style.display = ""
    }
}

const button = document.getElementById("dark-mode-button")
button.addEventListener("click", () => {
    document.body.classList.toggle("dark")
    let appearance = ""
    if (document.body.classList.contains("dark")) {
        appearance = "dark"
        button.innerHTML = "light mode"
    } else {
        button.innerHTML = "dark mode"
    }

    document.cookie = `appearance=${appearance}; SameSite=Strict;`
})

