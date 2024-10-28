import React from 'react';

import { ControlPosition } from 'leaflet';
import { RefreshCw } from 'lucide-react';
import { useMap } from 'react-leaflet';

import { DEFAULT_MAP_CENTER, DEFAULT_MAP_ZOOM } from '../constants';

import LeafletControl from './LeafletControl';



const PositionResetControl = ({ position }) => {
  const map = useMap();

  const handleOnClick = () => {
    map.setView(DEFAULT_MAP_CENTER, DEFAULT_MAP_ZOOM);
  };

  return (
    <LeafletControl position={position}>
      <button
        className="h-full w-full p-2 bg-white hover:bg-gray-100 transition-colors rounded-sm"
        onClick={handleOnClick}
      >
        <RefreshCw className="h-5 w-5" />
      </button>
    </LeafletControl>
  );
};

export default PositionResetControl;