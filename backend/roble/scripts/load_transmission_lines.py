import geopandas as gpd
from pathlib import Path
import requests 
from api.models.transmission import TransmissionLine
import pandas as pd
from pathlib import Path
from typing import Any
from typing import Dict
from django.contrib.gis.geos import GEOSGeometry
import shapely

import unicodedata
from api.constants import RP_AOI


STORE_PATH = Path(__file__).resolve().parent.parent.parent.parent / "static"
FILE_PATH = STORE_PATH / "38kv_transmission_lines"

def normalize_polygons(raw_gdf: gpd.GeoDataFrame, crs: int = 6566) -> gpd.GeoDataFrame:
    """
    Converts rows with multipolgons into multiple rows with polygons
    """
    return raw_gdf.explode('geometry')


COLUMN_MAP = {
    'FID': 'fid',
    'gid': 'gid',
    'region': 'region',
    'major_proj': 'major_proj',
    'asset_id': 'asset_id',
    'short_desc': 'short_desc',
    'fid_1': 'fid_1',
    'working': 'working',
    'circuit1': 'circuit1',
    'municipali': 'municipality',
    'planned_co': 'planned_cost',
    'estimated_': 'estimated_time', 
    'phasename': 'phase_name',
    'objectid': "object_id",
    "geometry": "geometry",
}
def strip_accents(text: str) -> str:
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore")  # type: ignore
    text = text.decode("utf-8")  # type: ignore
    return str(text)

def _clean_rows(entry):
    
    new_entry = {
        value: entry[key] if key in COLUMN_MAP.keys() else None
        for key, value in COLUMN_MAP.items()
    }
    new_entry["geometry"] = GEOSGeometry(
        shapely.to_wkt(new_entry["geometry"]), srid=6566
    )
    new_entry["asset_id"] = 0
    # new_entry["asset_id"] = None if new_entry["asset_id"] == "nan" else new_entry["asset_id"]
    new_entry["planned_cost"] = 0 
    new_entry["estimated_time"] = 0
    # new_entry["municipality"] = strip_accents(new_entry["municipality"]).upper()
    # new_entry["description"] = strip_accents(new_entry["description"]).upper()
    return new_entry

def run() -> None:

    gdf = gpd.read_file(FILE_PATH)
    gdf = gdf.to_crs('6566')
    aoi = gdf.from_features(RP_AOI["features"], crs=4236)
    aoi = aoi.to_crs("6566")


    j_gdf = gpd.clip(gdf, aoi)
    t_line_gdf = normalize_polygons(j_gdf)
    
    t_line_gdf = t_line_gdf.drop(columns=['Shape__Len'])
    
    t_line_list = []
    for _, entry in t_line_gdf.iterrows():
        new_entry = _clean_rows(entry)
        t_line_list.append(TransmissionLine(**new_entry))
        
    TransmissionLine.objects.bulk_create(t_line_list)
    