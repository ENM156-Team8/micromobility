function initialize() {
    var goo = google.maps,
        map = new goo.Map(document.getElementById('map-canvas'), {
            center: new goo.LatLng(52.52, 13.40),
            zoom: 10
        }),
        App = {
            map: map,
            bounds: new goo.LatLngBounds(),
            directionsService: new goo.DirectionsService(),
            directionsDisplays: []
        },
        colors = ['red', 'blue', 'yellow', 'green', 'purple']; // Add more colors if needed

    var waypoints = [
        {
            origin: '57.689784, 11.973249',
            destination: '57.727428, 12.004718',
            travelMode: google.maps.TravelMode.BICYCLING,
        },
        {
            origin: '57.727428, 12.004718',
            destination: '57.7295286, 12.0077593',
            travelMode: google.maps.TravelMode.WALKING,
        }
    ];

    for (var i = 0; i < waypoints.length; i++) {
        var directionsDisplay = new goo.DirectionsRenderer({
            map: map,
            preserveViewport: true,
            suppressMarkers: true,
            polylineOptions: { strokeColor: colors[i % colors.length], strokeWeight: 5},
            panel: document.getElementById('panel').appendChild(document.createElement('li'))
        });
        App.directionsDisplays.push(directionsDisplay);
        generateRoute(App.directionsService, waypoints[i], directionsDisplay);
    }

    function generateRoute(service, waypoint, display) {
        service.route(waypoint, function (result, status) {
            if (status == google.maps.DirectionsStatus.OK) {
                display.setDirections(result);
                App.map.fitBounds(App.bounds.union(result.routes[0].bounds));

                // Define the marker icons
                var icons = {
                    TRANSIT: './images/tram.png',
                    BICYCLING: './images/bike.png',
                    WALKING: './images/walk.png',
                    // Add more travel modes and corresponding icons as needed
                };

                // Add a marker at the start of the leg
                new google.maps.Marker({
                    position: result.routes[0].legs[0].start_location,
                    map: App.map,
                    icon: {
                        url: icons[waypoint.travelMode],
                        scaledSize: new google.maps.Size(40, 40) // Adjust the size as needed
                    }
                });
            }
        });
    }
}

google.maps.event.addDomListener(window, 'load', initialize);