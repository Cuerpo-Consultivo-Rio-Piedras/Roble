import React from 'react';

import classNames from 'classnames';
import { Loader2 } from 'lucide-react';

// import { Permit, Project, Property } from '../types';

// type Props = {
//   property: Property;
//   projects: Project[];
//   permits: Permit[];
//   isSelected: boolean;
//   isLoading: boolean;
//   className?: string;
// };

const SideBar = ({isLoading }) => {
  return (
    <div className={classNames('bg-gray-100 border-r py-2 px-2 overflow-y-scroll')}>
      {isLoading && <Loader2 size={30} className="animate-spin my-auto w-full h-full" />}
      <p>
          Esta es una herramienta para darle seguimiento a proyectos de construcción dudosos en las
          costas de Puerto Rico.
        </p>
    </div>
  );
};

export default SideBar;