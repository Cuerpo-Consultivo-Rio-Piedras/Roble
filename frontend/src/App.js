// import logo from './logo.svg';
// import './App.css';

import React, { useEffect, useState } from 'react';

import { MapContainer, TileLayer } from 'react-leaflet';
import SideBar from './Components/SideBar';
import POIMarker from './Components/POIMarker'
import { DEFAULT_MAP_CENTER, DEFAULT_MAP_ZOOM } from './constants';
import PositionResetControl from './Components/PositionResetControl';
import { API } from './Api';

import 'leaflet/dist/leaflet.css';

const api = new API()



function App() {
  // const [isSidebarLoading, setIsSidebarLoading] = useState(false);
  // const isSelected = selectedProperty !== null;
  const [isLoading, setIsLoading] = useState(true);
  const [pois, setpois] = useState(null)

  useEffect(() => {
    const fetch = async () => {
      const results = await api.listPOIs();
      console.log('api results', results)
      setpois(results);
      setIsLoading(false);
    };

    fetch();
  }, []);


  return (
    <div className="flex flex-col w-screen h-screen">
      <div className="bg-slate-300 px-2 py-1">
        <p className="text-3xl font-bold">Roble</p>
      </div>
      <div className="flex md:flex-row flex-col-reverse h-full">
      <SideBar
          className="md:w-72 w-full h-full"
          // property={selectedProperty}
          // projects={selectedPropertyProjects || []}
          // permits={selectedPropertyPermits || []}
          // isSelected={isSelected}
          // isLoading={isSidebarLoading}
        />
        <div className="w-full h-96 md:h-full">
          <MapContainer
            center={DEFAULT_MAP_CENTER}
            zoom={DEFAULT_MAP_ZOOM}
            className="h-full w-full outline-none"
            >
            <TileLayer
              url="https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png"
              className="map-tiles"
            />
            <PositionResetControl position="topright" />
            {isLoading ? null : pois.map(poi => {return (<POIMarker poi={poi} POIMarker/>)})}
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
