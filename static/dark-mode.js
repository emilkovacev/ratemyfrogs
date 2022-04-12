const toggle = (button) => {
    button.classList.toggle("bi-sun-fill");
    button.classList.toggle("bi-moon-fill");
    document.body.classList.toggle("dark-mode");
}

const add_copy_style = (button) => {
    button.classList.remove("bi-clipboard");
    button.classList.add("bi-clipboard-check");
    button.style.color = "green";
}

const remove_copy_style = (button) => {
    button.classList.add("bi-clipboard");
    button.classList.remove("bi-clipboard-check");
    button.style.color = "black";
}

const copy = (button) => {
    const text = document.getElementById("copy-url");
    navigator.clipboard.writeText(text.innerHTML);

    add_copy_style(button); 
    setTimeout(() => remove_copy_style(button), 2000);
}

const expand_frog = (img) => {
    const texts = document.getElementsByClassName("frog-text");
    img.classList.toggle("stretch");

    for (let text of texts) {
        text.classList.toggle("stretch");
    }

}

const light_button = document.getElementById("change-mode");
light_button.addEventListener("click", () => toggle(light_button));

const copy_button = document.getElementById("copy-button");
copy_button.addEventListener("click", () => copy(copy_button));

const frog_img = document.getElementsByClassName("frog-img")
for (let img of frog_img) {
    img.addEventListener("click", () => expand_frog(img));
}
