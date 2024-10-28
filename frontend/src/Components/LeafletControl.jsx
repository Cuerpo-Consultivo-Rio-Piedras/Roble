import React, { useEffect, useRef } from 'react';

import classNames from 'classnames';
import { ControlPosition } from 'leaflet';

const POSITION_CLASSES = {
  bottomleft: 'leaflet-bottom leaflet-left',
  bottomright: 'leaflet-bottom leaflet-right',
  topleft: 'leaflet-top leaflet-left',
  topright: 'leaflet-top leaflet-right',
};


const LeafletControl = ({ position, children, className }) => {
  const ref = useRef(null);

  useEffect(() => {
    const positionClass = (position && POSITION_CLASSES[position]) || POSITION_CLASSES.topright;

    const querySelectorSuffix = positionClass
      .split(' ')
      .map((str) => '.' + str)
      .join('');

    const container = document.querySelector('.leaflet-control-container ' + querySelectorSuffix);

    // We should put the attribution after the controls
    if (position == 'bottomright' || position === 'bottomleft') {
      container.prepend(ref.current);
    } else {
      container.appendChild(ref.current);
    }

    return () => {
      if (ref.current && container.contains(ref.current)) {
        container.removeChild(ref.current);
      }
    };
  }, [position]);

  return (
    // NOTE: We need `border-0` to expand the control to be filled by its children
    <div className={classNames('leaflet-control leaflet-bar border-0', className)} ref={ref}>
      {children}
    </div>
  );
};

export default LeafletControl;