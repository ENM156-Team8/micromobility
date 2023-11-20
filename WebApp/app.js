document.addEventListener('DOMContentLoaded', (event) => {
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

    document.getElementById('tripForm').addEventListener('submit', function(event) {
        event.preventDefault();

        var startLocation = document.querySelector("#startLocation").value;
        var destinationLocation = document.querySelector("#destinationLocation").value;

        fetch('http://localhost:5000/submitTrip', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                startLocation: startLocation,
                destinationLocation: destinationLocation,
            }),
        })
        .then(response => {
            console.log('Server Response:', response);
            return response.json();
        })
        .then(data => {
            console.log('Data:', data);
            document.querySelector("#output").innerHTML = data.message;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});