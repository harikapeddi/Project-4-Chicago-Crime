




d3.select("#model_result").on("click", function () {
    let crime = d3.select("#crime_dropdown").property('value')
    let location = d3.select("#location_dropdown").property('value')
    let season = d3.select("#season_dropdown").property('value')
    let hour = d3.select("#hour_dropdown").property('value')
    let lat = d3.select("#lat_dropdown").property('value')
    let lon = d3.select("#lon_dropdown").property('value')
    let domestic = d3.select("#dom_dropdown").property('value')
    console.log(`127.0.0.1:5000/results/${crime}/${location}/${season}/${hour}/${lat}/${lon}/${domestic}`)
    d3.json(`/results/${crime}/${location}/${season}/${hour}/${lat}/${lon}/${domestic}`)

        .then(function (data) {

            var arrest_prob = (data.prob[0][1] * 100).toFixed()
            document.getElementById('arrest_prob').innerHTML = arrest_prob + " %"
            // console.log(data)()
            console.log(data.result)
            console.log(`probability of arrest is ${(data.prob[0][1] * 100).toFixed(2)} %`)


        })
});

var mymap = L.map('map').setView([41.87, -87.62], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1IjoicXVpbGx5YSIsImEiOiJja3J2Y2QwZG0wNWF4MnBuMTVld2kyMzQ3In0.9pUO8Kx3WXzQJ_Amcn-VNw'
}).addTo(mymap);

var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at: " + e.latlng.toString())
        .openOn(mymap);
}
mymap.on('click', onMapClick);

mymap.on('click', function(e){
    var coord = e.latlng;
    var lat_c = coord.lat;
    var lng_c= coord.lng;
    d3.select("#lat_dropdown").attr('value', lat_c)
    d3.select("#lon_dropdown").attr('value', lng_c)
    console.log("You clicked the map at latitude: " + lat + " and longitude: " + lng);
    });