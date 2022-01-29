var latt = 50.6516;
var lngg = 80.6752;

function setCoords(latt,lngg){
    this.latt = latt;
    this.lngg = lngg;
    console.log(latt, lngg);
}

function initMap(){
    var userPos = {lat: latt, lng: lngg}
    var options = {
        zoom:18,
        center:userPos
    }

    var map = new google.maps.Map(document.getElementById('map'), options);

    addMarker({
    coords:{lat:29.5516, lng:-82.325},
    content:'<h1>I am a marker!</h1>'
    })

    function addMarker(props){
        marker = new google.maps.Marker({
          position: props.coords,
          map: map,
        });
        // check content
        if(props.content){
            var infoWindow = new google.maps.InfoWindow({
                content:props.content
            });
        }
        // event listener for marker
        marker.addListener('click', function(){
            infoWindow.open(map, marker);
        })
    }
}

function fillCoords(){
    document.getElementById("id_lat").value = latt;
    document.getElementById("id_long").value = lngg;
}

