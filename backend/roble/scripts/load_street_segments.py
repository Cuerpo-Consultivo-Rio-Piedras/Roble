import geopandas as gpd
from pathlib import Path
import requests 
from api.models.street import StreetSegment
import pandas as pd
from pathlib import Path
from typing import Any
from typing import Dict
from django.contrib.gis.geos import GEOSGeometry
import shapely

import unicodedata
from api.constants import RP_AOI


STORE_PATH = Path(__file__).resolve().parent.parent.parent.parent / "static"
FILE_PATH = STORE_PATH / "segment_data"

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


def normalize_polygons(raw_gdf: gpd.GeoDataFrame, crs: int = 6566) -> gpd.GeoDataFrame:
    """
    Converts rows with multipolgons into multiple rows with polygons
    """
    return raw_gdf.explode('geometry')


def _clean_rows(entry) -> Dict[str, Any]:
    """
    Steps:
        transforms columns
        converts geometry to django geometry
        cleans municipality
        cleans description

    returns dict
    """
    # TODO: Figure out how to store v_put metadata
    new_entry = {
        value: entry[key] if key in COLUMN_MAP.keys() else None
        for key, value in COLUMN_MAP.items()
    }
    new_entry["geometry"] = GEOSGeometry(
        shapely.to_wkt(new_entry["geometry"]), srid=6566
    )
    # new_entry["municipality"] = strip_accents(new_entry["municipality"]).upper()
    # new_entry["description"] = strip_accents(new_entry["description"]).upper()
    return new_entry

COLUMN_MAP = {
    "ID": "segment_id",
    "FENAME":"fe_name",
    "geometry": "geometry"
}


def run():
    print("loading fule")
    gdf = gpd.read_file(FILE_PATH)
    print("file loaded")
    gdf = gdf.to_crs('6566')
    aoi = gdf.from_features(RP_AOI["features"], crs=4236)
    aoi = aoi.to_crs("6566")


    j_gdf = gpd.clip(gdf, aoi)
    street_segment_gdf = normalize_polygons(j_gdf)
    print("segments", len(street_segment_gdf))
    
    street_segment_list = []
    for _, entry in street_segment_gdf.iterrows():
        new_entry = _clean_rows(entry)
        street_segment_list.append(StreetSegment(**new_entry))
        
    StreetSegment.objects.bulk_create(street_segment_list)
