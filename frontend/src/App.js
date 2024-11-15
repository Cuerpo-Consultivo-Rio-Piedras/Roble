import React, { useEffect, useState } from 'react';

import { MapContainer, TileLayer, LayersControl, LayerGroup } from 'react-leaflet';
import SideBar from './Components/SideBar';
import LandUseLayer from './Components/LandUseLayer';
import { DEFAULT_MAP_CENTER, DEFAULT_MAP_ZOOM } from './constants';
import PositionResetControl from './Components/PositionResetControl';
import { API } from './Api';

import 'leaflet/dist/leaflet.css';
import TransmissionLineLayer from './Components/TransmissionLineLayer';
import StreetLayer from './Components/StreetLayer';

const api = new API()

function App() {
  // const [isSidebarLoading, setIsSidebarLoading] = useState(false);
  // const isSelected = selectedProperty !== null;
  const [isLoading, setIsLoading] = useState(true);
  const [landUses, setLandUses] = useState(null);
  const [transmissionLines, setTransmissionLines] = useState(null);
  const [streets, setStreets] = useState(null);

  useEffect(() => {
    const fetch = async () => {
      const results = await api.listLandUse();
      setLandUses(results);
      // setIsLoading(false);
    };

    fetch();
  }, []);

  useEffect(() => {
    const fetch = async () => {
      const results = await api.listTransmissionLines();
      console.log('results', results)
      setTransmissionLines(results);
      // setIsLoading(false);
    };

    fetch();
  }, []);
  
  useEffect(() => {
    const fetch = async () => {
      const results = await api.listStreets();
      console.log('results', results)
      setStreets(results);
      // setIsLoading(false);
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
        />
        <div className="w-full h-96 md:h-full">
          <MapContainer
            center={DEFAULT_MAP_CENTER}
            zoom={DEFAULT_MAP_ZOOM}
            className="h-full w-full outline-none"
            maxZoom={25}
            >
            <TileLayer
              url="https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png"
              className="map-tiles"
            />
            <PositionResetControl position="topright" />
            <LayersControl position="topright">
              <LayersControl.Overlay name="PUT">
                <LayerGroup>
                  {landUses == null ? null : landUses.map((landUse) => (
                    <LandUseLayer
                      key={landUse.id}
                      landUse={landUse}
                      // onSelectedPropertyChange={handleOnSelectedPropertyChange}
                    />
                  ))}
                </LayerGroup>
              </LayersControl.Overlay>
              
              <LayersControl.Overlay name="Lineas de Transmission">
                <LayerGroup>
                  {transmissionLines == null ? null : transmissionLines.map((landUse) => (
                    <TransmissionLineLayer
                      key={landUse.id}
                      landUse={landUse}
                      // onSelectedPropertyChange={handleOnSelectedPropertyChange}
                    />
                  ))}
                </LayerGroup>
              </LayersControl.Overlay>
              
              <LayersControl.Overlay name="Carreteras">
                <LayerGroup>
                  {streets == null ? null : streets.map((street) => (
                    <StreetLayer
                      key={street.id}
                      street={street}
                      // onSelectedPropertyChange={handleOnSelectedPropertyChange}
                    />
                  ))}
                </LayerGroup>
              </LayersControl.Overlay>
                
            </LayersControl>
          </MapContainer>
        </div>
      </div>
    </div>
  );
}

export default App;
