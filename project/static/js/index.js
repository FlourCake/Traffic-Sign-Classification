var file = document.getElementById("file"),
    button = document.getElementById("submit");

file.onchange = function() {
    (file.files.length == 0) ? button.disabled = true : button.disabled = false;
};