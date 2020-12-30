const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map')
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
const locations = JSON.parse(document.getElementById('locations-data').textContent);
let feature = L.geoJSON(locations).bindPopup(function (layer) { return layer.feature.properties.place; }).addTo(map);
map.fitBounds(feature.getBounds(), { padding: [100, 100] });

