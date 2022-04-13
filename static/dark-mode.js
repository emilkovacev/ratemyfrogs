const toggle = (button) => {
    button.classList.toggle("bi-sun-fill");
    button.classList.toggle("bi-moon-fill");
    document.body.classList.toggle("dark-mode");

    if (document.body.classList.contains("dark-mode")) {
        console.log("set dark mode");
        setCookie("mode", "dark-mode", 20);
    } else {
        setCookie("mode", "light-mode", 20);
        console.log("set light mode");
    }
}

const get_mode = () => {
    console.log('setting mode...');
    const button = document.getElementById("change-mode");
    const mode = getCookie("mode");
    if (mode == "dark-mode") {
        console.log(mode);
        toggle(button);
    }
}

const add_copy_style = (button) => {
    button.classList.remove("bi-clipboard");
    button.classList.add("bi-clipboard-check");
    button.stylecolor = "green";
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

function setCookie(cname, cvalue, max_days) {
  let max_age = "max-age=" + max_days*24*60*60;
  document.cookie = cname + "=" + cvalue + ";" + max_age + ";samesite=lax";
}

function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

const button = document.getElementById("change-mode");
button.addEventListener("click", () => toggle(button));

const copy_button = document.getElementById("copy-button");
copy_button.addEventListener("click", () => copy(copy_button));

const frog_img = document.getElementsByClassName("frog-img");
for (let img of frog_img) {
    img.addEventListener("click", () => expand_frog(img));
}

document.addEventListener("load", get_mode());
