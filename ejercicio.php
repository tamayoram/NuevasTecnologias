
<?php

//solo un cambio
$pasajerosBello=0;
$pasajerosSabaneta=0;
$pasajerosSanJavier=0;
$pasajerosTotal=0;

$nuevosBello=0;
$nuevosSabaneta=0;
$nuevosSanJavier=0;

// para parar el ciclo se debe utilizar el número 99999 que se le presentara al usuario por pantalla

while ($nuevosBello!=99999){

    $pasajerosBello=$pasajerosBello+$nuevosBello;
    
    //Se debe leer de nuevo la variables $nuevosBello si se lee de una base de datos o directamente de un formulario. Esta lectura permite definir el valor que se va a agregar y si es 99999 se para el ciclo.
}

while ($nuevosSabaneta!=99999){

    $pasajerosSabaneta=$pasajerosSabaneta+$nuevosSabaneta;
    
    //Se debe leer de nuevo la variables $nuevosSabaneta si se lee de una base de datos o directamente de un formulario. Esta lectura permite definir el valor que se va a agregar y si es 99999 se para el ciclo.

}

while ($nuevosSanJavier!=99999){

    $pasajerosSanJavier=$pasajerosSanJavier+$nuevosSanJavier;
    
    // Se debe leer de nuevo la variables $nuevosBello si se lee de una base de datos o directamente de un formulario. Esta lectura permite definir el valor que se va a agregar y si es 99999 se para el ciclo.
}


// Se calcula el total de pasajeros
$pasajerosTotal=$pasajerosBello+$pasajerosSabaneta+$pasajerosSanJavier;

//Se presenta cada uno de los valores
echo "El total de pasajeros en Bello es = <b> ".$pasajerosBello."</b></br> ";
echo "El total de pasajeros en Sabaneta es = <b> ".$pasajerosSabaneta."</b></br> ";
echo "El total de pasajeros en San Javier es = <b> ".$pasajerosSanJavier."</b></br> ";
echo "El valor de pasajeros es = <b> ".$pasajerosTotal."</b></br> ";

?>