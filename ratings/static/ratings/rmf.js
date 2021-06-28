function myFunction() {
  /* Get the text field */
  var copyText = document.getElementById("frog-url");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");
  button = document.getElementById("copy-button")
  button.value = "copied!"
  button.style.borderColor = "rgb(25, 190, 60)"
  button.style.color = "rgb(25, 190, 60)"
  button.id = "copy-button-no-hover"
  button.onclick = ""
}
