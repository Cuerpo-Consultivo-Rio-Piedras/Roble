
export class API {
    BASE_URI = process.env.REACT_APP_BACKEND_URI;
    POI_ENDPOINT = '/poi';
    LAND_USE_ENDPOINT = '/landuse'
    TRANSMISSION_LINE_ENDPOINT = "/transmission_line"
    STREET_ENDPOINT = "/street"

    listLandUse = async () => {
        try {
          const response = await fetch("http://localhost:8000/api"+ this.LAND_USE_ENDPOINT, {
            method: 'GET',
            redirect: 'follow',
          });
          return await response.json();
        } catch (e) {
          console.log(e)
          throw new Error(e);
        }
      };
    
    listTransmissionLines = async () => {
      try {
        const response = await fetch("http://localhost:8000/api"+ this.TRANSMISSION_LINE_ENDPOINT, {
          method: 'GET',
          redirect: 'follow',
        });
        return await response.json();
      } catch (e) {
        console.log(e)
        throw new Error(e);
      }
    };
    listStreets = async () => {
      try {
        const response = await fetch("http://localhost:8000/api"+ this.STREET_ENDPOINT, {
          method: 'GET',
          redirect: 'follow',
        });
        return await response.json();
      } catch (e) {
        console.log(e)
        throw new Error(e);
      }
    };
}