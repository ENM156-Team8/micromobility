
const x = document.getElementById("displayStartLocation");
const startLocationInput = document.getElementById("startLocation");

window.getLocation = function() {
    const x = document.getElementById("displayStartLocation");
    const startLocationInput = document.getElementById("startLocation");

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }

    function showPosition(position) {
        const coords = position.coords.latitude + ", " + position.coords.longitude;
        x.innerHTML = coords;
        startLocationInput.value = coords;
    }
}