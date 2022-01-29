function initMap(){
    var Gainesville = {lat:29.6516, lng:277.6752};
    var options = {
        zoom:13,
        center:Gainesville
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

