import React from 'react';

import L from 'leaflet';
import { GeoJSON, useMap } from 'react-leaflet';



// TODO: maybe randomize this thing?
const setColor = () => {
  return {
    weight: 5,
    stroke: true,
    color: 'green',
    fillColor: 'green',
  };
};

const TransmissionLineLayer = ({ landUse, onSelectedPropertyChange }) => {
  const map = useMap();
  // const handleOnClick = () => {
  //   const multipolygon = L.geoJson(landUse.geometry);
  //   map.fitBounds(multipolygon.getBounds(), { animate: true });
  //   onSelectedPropertyChange(property);
  // };

  return (
    <GeoJSON
      data={landUse.geometry}
      style={setColor}
      // eventHandlers={{
      //   click: handleOnClick,
      // }}
    />
  );
};

export default TransmissionLineLayer;
