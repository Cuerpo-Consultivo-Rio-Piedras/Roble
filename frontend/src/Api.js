
export class API {
    BASE_URI = process.env.REACT_APP_BACKEND_URI;
    POI_ENDPOINT = '/poi';

    listPOIs = async () => {
        try {
          console.log(this.BASE_URI, this.POI_ENDPOINT)
          const response = await fetch("http://localhost:8000/api"+ this.POI_ENDPOINT, {
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