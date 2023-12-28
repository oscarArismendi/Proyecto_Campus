function getText(nombre) {
    var userInput = document.getElementById(nombre);
    var enteredText = userInput.value;
    return enteredText

}
var button = document.querySelector("#boton_subir");
var input_titulo = getText("input_titulo");
var input_subtitulo = getText("input_subtitulo");
button.addEventListener("click",() => {
    var input_titulo = getText("input_titulo");
    var input_subtitulo = getText("input_subtitulo");
    console.log(input_titulo)
    console.log(input_subtitulo)
} );

