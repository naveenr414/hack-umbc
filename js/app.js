// Initialize and add the map
function initMap() {
  // The location of Uluru
  var center_us = {lat: 41.850033, lng: -87.6500523};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 4.5, center: center_us});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: center_us, map: map});
}

// trigger for modal
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
  });