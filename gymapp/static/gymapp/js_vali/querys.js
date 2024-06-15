$(document).ready(function () {
    console.log("Esperando datos......");

    $.getJSON('https://mindicador.cl/api', function(data) {
        $(".spinner-border").hide();
        $(".textloader").hide();
        
        $("#dolar").text('$' + data.dolar.valor);
        $("#uf").text("$" + data.uf.valor);
        $("#bitcoin").text("$" + data.bitcoin.valor);
    }).fail(function() {
        console.log('Error al consumir la API!');
        $("#dolar").text("No se pudo obtener");
        $("#uf").text("No se pudo obtener");
        $("#bitcoin").text("No se pudo obtener");
        $("#dolar, #uf, #bitcoin").addClass("text-danger h6");
    });
});