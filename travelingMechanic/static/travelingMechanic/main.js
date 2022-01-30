var latt=29.6516;
var lngg=-82.3248;

function setCoords(latt, lngg){
    this.latt = latt;
    this.lngg = lngg;
}

function fillCoords(){
    document.getElementById("id_lat").value = latt;
    document.getElementById("id_long").value = lngg;
}
