import React, { useEffect, useState } from 'react';

import { MapContainer, TileLayer, LayersControl, LayerGroup, GeoJSON } from 'react-leaflet';
import SideBar from './Components/SideBar';
import { DEFAULT_MAP_CENTER, DEFAULT_MAP_ZOOM } from './constants';
import PositionResetControl from './Components/PositionResetControl';

import 'leaflet/dist/leaflet.css';


function App() {
  const [streets, setStreets] = useState(null);
  const [parcels, setParcels] = useState(null);

  useEffect(() => {
    const fetchParcels = async () => {
      const results = await fetch("parcel.geojson");
      const parcels = await results.json()
      setParcels(parcels);
    };

    fetchParcels();
  }, []);
  
  useEffect(() => {
    const fetchData = async () => {
      const results = await fetch("street_segment.geojson");
      const streetSegments = await results.json()
      setStreets(streetSegments);
    };

    fetchData();
  }, []);
  return (
    <div className="flex flex-col w-screen h-screen">
      <div className="bg-slate-300 px-2 py-1">
        <p className="text-3xl font-bold">Roble</p>
      </div>
      <div className="flex md:flex-row flex-col-reverse h-full">
      <SideBar
          className="md:w-72 w-full h-full"
        />
        <div className="w-full h-96 md:h-full">
          <MapContainer
            center={DEFAULT_MAP_CENTER}
            zoom={DEFAULT_MAP_ZOOM}
            className="h-full w-full outline-none"
            // minZoom={16}
            // maxZoom={18}
            >
            <TileLayer
              url="https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png"
              className="map-tiles"
            />
            <PositionResetControl position="topright" />
            <LayersControl position="topright">              
              <LayersControl.Overlay name="Parcelas">
                  {parcels && (
                    <GeoJSON key={1} data={parcels}>

                    </GeoJSON>)
                  }
              </LayersControl.Overlay>
              
              <LayersControl.Overlay name="Carreteras">
                  {streets && (
                    <GeoJSON key={2} data={streets}>

                    </GeoJSON>)
                  }
                  
              </LayersControl.Overlay>
                
            </LayersControl>
          </MapContainer>
        </div>
      </div>
    </div>
  );
}

export default App;