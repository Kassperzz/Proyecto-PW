//Validacion RUT
document.getElementById("myFrom").addEventListener("submit", function(event){
    var rut = document.getElementById("rut").value;
    if (!validacion(rut)){
        alert("El RUT ingresado no es valido");
        event.preventDefault();
    }
});
function validarRut(rut) {
    if (rut.length !== 10) {
        return false;
    }
}

var rutSinGuion = rut.replace("-","");
var rutSinDV  = rutSionGuion.slice(o, -1);
var dv = rutSinGuion.slice(-1).toUpperCase;

if(!/^[0-9]+$/g.test(rutSinDV)) {
    return false;
}

var suma =  0;
var factor = 2;

for(var i = rutSinDV.length - 1; i >= 0; i--) {
    suma+= factor * parseInt(rutSinDV.charAt(i));
    factor=factor % 7 === 0 ? 2 : factor + 1;
}

var dvCalculado = 11 - (suma % 11);
dvCalculado = dvCalculado === 11 ? "0" : dvCalculado === 10 ? "K" : dvCalculado.toString();
return dv === dvCalculado;