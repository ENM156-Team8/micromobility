
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

document.addEventListener('DOMContentLoaded', (event) => {
    // Check if the cookie exists and set the initial mode
    var lightModeCookie = document.cookie.split('; ').find(row => row.startsWith('light-mode'));
    var modeSwitcher = document.getElementById('mode-switcher');
    if (lightModeCookie) {
        var lightMode = lightModeCookie.split('=')[1];
        document.body.classList.toggle('light-mode', lightMode === 'true');
        // Update the switch's position based on the mode
        modeSwitcher.checked = lightMode === 'true';
    }

    modeSwitcher.addEventListener('click', function() {
        // Toggle the mode
        var isLightMode = document.body.classList.toggle('light-mode');

        // Set the cookie to store the mode
        var date = new Date();
        date.setFullYear(date.getFullYear() + 10); // Set the date one year from now
        document.cookie = `light-mode=${isLightMode}; SameSite=None; Secure; expires=${date.toUTCString()}; path=/`;

        // Update the switch's position based on the mode
        this.checked = isLightMode;
    });
});


function submitTrip() {
    document.getElementById("noTripsText").innerText = "Laddar resor...";
}