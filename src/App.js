// import logo from './logo.svg';
// import './App.css';

import React, { useEffect, useState } from 'react';

import { MapContainer, TileLayer } from 'react-leaflet';
import SideBar from './components/SideBar';
import { DEFAULT_MAP_CENTER, DEFAULT_MAP_ZOOM } from './constants';
import PositionResetControl from './components/PositionResetControl';

import 'leaflet/dist/leaflet.css';


function App() {
  // const [isSidebarLoading, setIsSidebarLoading] = useState(false);
  // const isSelected = selectedProperty !== null;


  return (
    <div className="flex flex-col w-screen h-screen">
      <div className="bg-slate-300 px-2 py-1">
        <p className="text-3xl font-bold">Programando Con Conciencia</p>
        <p className="text-xl font-normal">Construcciones Cuestionables en la Costa</p>
      </div>
      <div className="flex md:flex-row flex-col-reverse h-full">
        <div className="w-full h-96 md:h-full">
          <MapContainer
            center={DEFAULT_MAP_CENTER}
            zoom={10}
            className="h-full w-full outline-none"
            >
            <TileLayer
              url="https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png"
              className="map-tiles"
            />
            {/* <PositionResetControl position="topright" /> */}
            {/* <LayerLegend position="bottomright" /> */}
            {/* <ReportMarkerLegend position="bottomleft" /> */}

            {/* {observations.map((observation) => (
              <ObservationMarker key={observation.id} observation={observation} />
            ))} */}

            {/* {properties.map((property) => (
              <PropertyLayer
                key={property.id}
                property={property}
                onSelectedPropertyChange={handleOnSelectedPropertyChange}
              />
            ))} */}

            {/* {parcels.map((parcel) => (
              <ParcelLayer key={parcel.id} parcel={parcel} />
            ))} */}
          </MapContainer>
        </div>
      </div>
    </div>
  );
}

export default App;
