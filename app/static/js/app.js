// Initialize and add the map
function initMap() {
  // The location of Uluru
  var center_us = {lat: 41.850033, lng: -87.6500523};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {
                                        zoom: 4.5,
                                        center: center_us,
                                        minZoom: 4.5
                                      });
  // var kmlSource = 'https://github.com/naveenr414/hack-umbc/blob/master/app/templates/kml/2012_US_Congressional_Districts.kml';

  // var kmlLayer = new google.maps.KmlLayer(kmlSource, {
  //   suppressInfoWindows: true,
  //   preserveViewport: false,
  //   map: map
  // });

  map.addListener("click", function (event) {
      var latitude = event.latLng.lat();
      var longitude = event.latLng.lng();
      getDataLong(latitude,longitude);
  });
}

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems);
});

function getData(address){
	var data = new FormData();
	data.append("address",address);
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "http://127.0.0.1:5000/address", true);
	xhr.onload = function () {
    // do something to response
    alert(this.responseText);
};
	xhr.send(data);
}

function getDataLong(lat,lon){
	var data = new FormData();
	data.append("lat",lat);
	data.append("lon",lon);
	var xhr = new XMLHttpRequest();
	xhr.open("POST", "http://127.0.0.1:5000/address", true);
	xhr.onload = function () {
    // do something to response
    alert(this.responseText);
};
	xhr.send(data);
}

// function searchAddress(ele) {
//   if(event.key === 'Enter') {
//     var places
//     console.log(ele.suggestion);
//   }
// }
