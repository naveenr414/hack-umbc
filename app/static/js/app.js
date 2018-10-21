var map;

// Initialize and add the map
function initMap() {
  // The location of the US
  var center_us = {lat: 41.850033, lng: -87.6500523};
  // The map, centered at the US
  map = new google.maps.Map(
      document.getElementById('map'), {
                                        zoom: 4.5,
                                        center: center_us,
                                        minZoom: 4.5,
                                        styles: CustomMapStyles
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
    parseReturnData(this.responseText);
    //alert(response);
  };
	xhr.send(data);
}

function parseReturnData(response) {
  //alert(response)
  var result = JSON.parse(response)
  var senate_info = result['senate'][0]
  var governor_info = result['governor'][0]
  var house_info = result['house'][0]
  $("#render_modal").trigger("click")
  var senate_cand1 = senate_info['candidates'][0];
  var senate_cand2 = senate_info['candidates'][1];
  var governor_cand1 = governor_info['candidates'][0];
  var governor_cand2 = governor_info['candidates'][1];
  $(".modal-content").html("<h4>" + senate_info['state'] + "</h4>" +
                           "<b>Senate</b> " + "<br><ul><li><em>" + senate_cand1['name'] + "</em> (" + senate_cand1['party'] + ") </li>"
                                                                     + "&emsp;- " + senate_cand1['position_1']
                                                                     + "<li><em>" + senate_cand2['name'] + "</em> (" + senate_cand2['party'] + ") </li>"
                                                                     + "&emsp;- " + senate_cand2['position_1'] + "</ul>" +
                           "<br><b>Governor</b> " + "<br><ul><li><em>" + governor_cand1['name'] + "</em> (" + governor_cand1['party'] + ") </li>"
                                                                     + "&emsp;- " + governor_cand1['position_1']
                                                                     + "<li><em>" + governor_cand2['name'] + "</em> (" + governor_cand2['party'] + ") </li>"
                                                                     + "&emsp;- " + governor_cand2['position_1'] + "</ul>");
}

// function searchAddress(ele) {
//   if(event.key === 'Enter') {
//     var places
//     console.log(ele.suggestion);
//   }
// }

$(document).ready( () => {
  $("#render_modal").on("click", function () {
  });
});

$(document).ready(function(){
   $("#fireme").click(function(){
       $("#modal1").modal("toggle");
       $("#modal1").show();
   });
});

var CustomMapStyles = [
 {
   "elementType": "geometry",
   "stylers": [
     {
       "color": "#f5f5f5"
     }
   ]
 },
 {
   "elementType": "labels.icon",
   "stylers": [
     {
       "visibility": "off"
     }
   ]
 },
 {
   "elementType": "labels.text.fill",
   "stylers": [
     {
       "color": "#616161"
     }
   ]
 },
 {
   "elementType": "labels.text.stroke",
   "stylers": [
     {
       "color": "#f5f5f5"
     }
   ]
 },
 {
   "featureType": "administrative.country",
   "elementType": "geometry.stroke",
   "stylers": [
     {
       "color": "#110f00"
     },
     {
       "weight": 1.5
     }
   ]
 },
 {
   "featureType": "administrative.land_parcel",
   "elementType": "labels.text.fill",
   "stylers": [
     {
       "color": "#bdbdbd"
     }
   ]
 },
 {
   "featureType": "administrative.province",
   "elementType": "geometry.stroke",
   "stylers": [
     {
       "color": "#110f00"
     },
     {
       "weight": 1.5
     }
   ]
 },
 {
   "featureType": "poi",
   "elementType": "geometry",
   "stylers": [
     {
       "color": "#eeeeee"
     }
   ]
 },
 {
   "featureType": "poi",
   "elementType": "labels.text",
   "stylers": [
     {
       "visibility": "off"
     }
   ]
 },
 {
   "featureType": "poi",
   "elementType": "labels.text.fill",
   "stylers": [
     {
       "color": "#757575"
     }
   ]
 },
 {
   "featureType": "poi.business",
   "stylers": [
     {
       "visibility": "off"
     }
   ]
 },
 {
   "featureType": "poi.park",
   "elementType": "geometry",
   "stylers": [
     {
       "color": "#e5e5e5"
     }
   ]
 },
 {
   "featureType": "poi.park",
   "elementType": "labels.text.fill",
   "stylers": [
     {
       "color": "#9e9e9e"
     }
   ]
 },
 {
   "featureType": "road",
   "stylers": [
     {
       "visibility": "off"
     }
   ]
 },
 {
   "featureType": "road",
   "elementType": "geometry",
   "stylers": [
     {
       "color": "#ffffff"
     }
   ]
 },
 {
   "featureType": "road",
   "elementType": "labels.icon",
   "stylers": [
     {
       "visibility": "off"
     }
   ]
 },
 {
   "featureType": "road.arterial",
   "elementType": "labels.text.fill",
   "stylers": [
     {
       "color": "#757575"
     }
   ]
 },
 {
   "featureType": "road.highway",
   "elementType": "geometry",
   "stylers": [
     {
       "color": "#dadada"
     }
   ]
 },
 {
   "featureType": "road.highway",
   "elementType": "labels.text.fill",
   "stylers": [
     {
       "color": "#616161"
     }
   ]
 },
 {
   "featureType": "road.local",
   "elementType": "labels.text.fill",
   "stylers": [
     {
       "color": "#9e9e9e"
     }
   ]
 },
 {
   "featureType": "transit",
   "stylers": [
     {
       "visibility": "off"
     }
   ]
 },
 {
   "featureType": "transit.line",
   "elementType": "geometry",
   "stylers": [
     {
       "color": "#e5e5e5"
     }
   ]
 },
 {
   "featureType": "transit.station",
   "elementType": "geometry",
   "stylers": [
     {
       "color": "#eeeeee"
     }
   ]
 },
 {
   "featureType": "water",
   "elementType": "geometry",
   "stylers": [
     {
       "color": "#c9c9c9"
     }
   ]
 },
 {
   "featureType": "water",
   "elementType": "geometry.fill",
   "stylers": [
     {
       "color": "#474645"
     }
   ]
 },
 {
   "featureType": "water",
   "elementType": "labels.text.fill",
   "stylers": [
     {
       "color": "#9e9e9e"
     }
   ]
 }
]