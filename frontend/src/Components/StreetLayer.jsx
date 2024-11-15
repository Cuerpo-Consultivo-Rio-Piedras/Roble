import React from 'react';

import L from 'leaflet';
import { GeoJSON, useMap } from 'react-leaflet';



// TODO: maybe randomize this thing?
const setColor = () => {
  return {
    weight: 3,
    stroke: true,
    color: '#1f3a93',
    fillColor: '#1f3a93',
  };
};

const StreetLayer = ({ street, onSelectedPropertyChange }) => {
  const map = useMap();
  // const handleOnClick = () => {
  //   const multipolygon = L.geoJson(landUse.geometry);
  //   map.fitBounds(multipolygon.getBounds(), { animate: true });
  //   onSelectedPropertyChange(property);
  // };

  return (
    <GeoJSON
      data={street.geometry}
      style={setColor}
      // eventHandlers={{
      //   click: handleOnClick,
      // }}
    />
  );
};

export default StreetLayer;
