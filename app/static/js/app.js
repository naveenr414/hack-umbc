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
  var kmlSource = 'https://github.com/naveenr414/hack-umbc/blob/master/app/templates/kml/2012_US_Congressional_Districts.kml';

  var kmlLayer = new google.maps.KmlLayer(kmlSource, {
    suppressInfoWindows: true,
    preserveViewport: false,
    map: map
  });
}

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems);
});

var placesAutocomplete = places({
  container: document.querySelector('#address-input')
});

places(placesAutocomplete);