import React from 'react';

import { Marker, Popup, useMap, GeoJSON } from 'react-leaflet';

import { createIconWithColor } from '../utils';


const POIMarker = ({ poi }) => {
  console.log("aca",poi);
  const map = useMap();

  const icon = createIconWithColor("red");
  const location = [poi.location.coordinates[1], poi.location.coordinates[0]];

  const onClick = (event) => {
    const { lat: observationLatitude, lng: observationLongitude } = event.latlng;
    map.setView([observationLatitude, observationLongitude], 17);
  };

  return (
    <Marker
      position={location}
      icon={icon}
      eventHandlers={{
        click: onClick,
      }}
    >
      <Popup>
        <div className="space-y-2">
          <div>
            <h4 className="mb-0 font-semibold">Nombre</h4>
            <p className="!my-0">{poi.name}</p>
          </div>
        </div>
      </Popup>
    </Marker>
  );
};

export default POIMarker;