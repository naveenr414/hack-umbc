var map;
var response;

// Initialize and add the map
function initMap() {
  // The location of the US
  var center_us = {lat: 41.850033, lng: -87.6500523};
  // The map, centered at the US
  map = new google.maps.Map(
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

  function zoomIn(lat,lng) {
    map.setZoom(15);
    map.setCenter({lat: lat,
                   lng: lng});
  }

  map.addListener("click", function (event) {
      var latitude = event.latLng.lat();
      var longitude = event.latLng.lng();
      console.log(latitude + ", " + longitude);
      getDataLong(latitude,longitude);
  });
}

function zoomIn(lat,lng) {
  map.setZoom(8);
  map.setCenter({lat: lat,
                 lng: lng});
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
    //let a = this.responseText
		alert(this.responseText);
    return this.responseText;
    //alert(response);
  };
	xhr.send(data);
}

function parseReturnData() {
  //alert(response)
  var result = JSON.parse(response)
  console.log(result)
}

// function searchAddress(ele) {
//   if(event.key === 'Enter') {
//     var places
//     console.log(ele.suggestion);
//   }
// }


