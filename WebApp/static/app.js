
// autocomplete and geocode address using google maps api
function initMaps() {
    // set default bounds to Gothenburg
    const defaultBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(57.689461, 11.973725),
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
    if (document.getElementById("noTripsText") != null) {
        document.getElementById("noTripsText").innerHTML = '<div class="center-noTripsText">Laddar resor<span id="wait">.</span></div>';
    }
    var dots = window.setInterval( function() {
        var wait = document.getElementById("wait");
        if ( wait.innerHTML.length > 3 ) 
            wait.innerHTML = "";
        else 
            wait.innerHTML += ".";
        }, 500);
}



var darkModeStyles = [
    { elementType: 'geometry', stylers: [{ color: '#242f3e' }] },
    { elementType: 'labels.text.stroke', stylers: [{ color: '#242f3e' }] },
    { elementType: 'labels.text.fill', stylers: [{ color: '#746855' }] },
    {
        featureType: 'administrative.locality',
        elementType: 'labels.text.fill',
        stylers: [{ color: '#d59563' }]
    },
    {
        featureType: 'poi',
        elementType: 'labels.text.fill',
        stylers: [{ color: '#d59563' }]
    },
    {
        featureType: 'poi.park',
        elementType: 'geometry',
        stylers: [{ color: '#263c3f' }]
    },
    {
        featureType: 'poi.park',
        elementType: 'labels.text.fill',
        stylers: [{ color: '#6b9a76' }]
    },
    {
        featureType: 'road',
        elementType: 'geometry',
        stylers: [{ color: '#38414e' }]
    },
    {
        featureType: 'road',
        elementType: 'geometry.stroke',
        stylers: [{ color: '#212a37' }]
    },
    {
        featureType: 'road',
        elementType: 'labels.text.fill',
        stylers: [{ color: '#9ca5b3' }]
    },
    {
        featureType: 'road.highway',
        elementType: 'geometry',
        stylers: [{ color: '#746855' }]
    },
    {
        featureType: 'road.highway',
        elementType: 'geometry.stroke',
        stylers: [{ color: '#1f2835' }]
    },
    {
        featureType: 'road.highway',
        elementType: 'labels.text.fill',
        stylers: [{ color: '#f3d19c' }]
    },
    {
        featureType: 'transit',
        elementType: 'geometry',
        stylers: [{ color: '#2f3948' }]
    },
    {
        featureType: 'transit.station',
        elementType: 'labels.text.fill',
        stylers: [{ color: '#d59563' }]
    },
    {
        featureType: 'water',
        elementType: 'geometry',
        stylers: [{ color: '#17263c' }]
    },
    {
        featureType: 'water',
        elementType: 'labels.text.fill',
        stylers: [{ color: '#515c6d' }]
    },
    {
        featureType: 'water',
        elementType: 'labels.text.stroke',
        stylers: [{ color: '#17263c' }]
    },
    {
        featureType: 'poi',
        elementType: 'all',
        stylers: [{ visibility: 'off' }]
    }
]

var lightModeStyles = [
    {
        featureType: 'poi',
        elementType: 'all',
        stylers: [{ visibility: 'off' }]
    }
]

