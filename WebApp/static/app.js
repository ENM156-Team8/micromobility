
// autocomplete and geocode address using google maps api
function initMaps() {
    // set default bounds to Gothenburg
    const defaultBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(57.7075, 11.9675),
    );
    const countryRestrict = { country: "se" };

    // autocomplete and geocoding for start location
    $("#startLocation").geocomplete({
        bounds: defaultBounds,
        componentRestrictions: countryRestrict
    })
    .bind("geocode:result", function(event, result){
        var latLng = result.geometry.location.lat() + "," + result.geometry.location.lng();
        $("#startLocationCoords").val(latLng);
        console.log(latLng);
    });

    // autocomplete and geocoding for destination location
    $("#destinationLocation").geocomplete({
        bounds: defaultBounds,
        componentRestrictions: countryRestrict
    })
    .bind("geocode:result", function(event, result){
        var latLng = result.geometry.location.lat() + "," + result.geometry.location.lng();
        $("#destinationLocationCoords").val(latLng);
        console.log(latLng);
    });

    // trigger geocoding when find button is clicked
    $("#find").click(function(event){
        $("#startLocation").trigger("geocode");
        $("#destinationLocation").trigger("geocode");
    });
}
