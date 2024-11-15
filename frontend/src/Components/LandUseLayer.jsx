import React from 'react';

import L from 'leaflet';
import { GeoJSON, useMap } from 'react-leaflet';



// TODO: maybe randomize this thing?
const setColor = (clasiPut) => {
  switch(clasiPut){
    case "AGUA":
      return {
        weight: 5,
        stroke: true,
        color: 'blue',
        fillColor: 'blue',
      };
    
    case "VIAL":
      return {
        weight: 1,
        stroke: true,
        color: 'black',
        fillColor: 'black',
        fillOpacity: .25
      };
    
    case "SU":
      return {
        weight: 2,
        stroke: false,
        color: 'red',
        fillColor: "#f7c09a",
        fillOpacity: .4
      };
  }
  
};

const LandUseLayer = ({ landUse, onSelectedPropertyChange }) => {
  const map = useMap();
  // const handleOnClick = () => {
  //   const multipolygon = L.geoJson(landUse.geometry);
  //   map.fitBounds(multipolygon.getBounds(), { animate: true });
  //   onSelectedPropertyChange(property);
  // };
  const style = setColor(landUse.clasi_put)
  return (
    <GeoJSON
      data={landUse.geometry}
      style={style}
      // eventHandlers={{
      //   click: handleOnClick,
      // }}
    />
  );
};

export default LandUseLayer;
