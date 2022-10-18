import json

from collective.contentsections.sections.base import SectionView
from plone import api


class LocationsSectionView(SectionView):
    """LocationsSection view"""

    @property
    def data_pat_leaflet(self):
        data =  {
            "fullscreencontrol": True,
            "zoomcontrol": True
        }
        return json.dumps(data)

    @property
    def data_geojson(self):
        # TODO : use locations
        features = [
            {
                "type": "Feature",
                "properties": {"popup": "ICI"},
                "geometry": {"type": "Point", "coordinates": [15.4382918, 47.0708101]}
            }
        ]
        data =  {
            "type": "FeatureCollection",
            "features": features
        }
        return json.dumps(data)

    @property
    def locations(self):
        brains = api.content.find(context=self.context, depth=1, portal_type="collective.contentsections.Location")
        results = [
            {
                "title": brain.Title,
                "description": brain.Description,
                "latitude": brain.latitude,
                "longitude": brain.longitude,
                "lead_image_url": f"{brain.getURL()}/@@images/image/mini" if brain.image_scales else None,
            }
            for brain in brains
        ]
        return results
