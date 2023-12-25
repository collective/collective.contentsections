import json

from plone import api
from plone.memoize import view

from collective.contentsections.sections.base import SectionView


class LocationsSectionView(SectionView):
    """LocationsSection view"""

    @property
    @view.memoize
    def center(self):
        if not self.locations:
            return (0.0, 0.0)
        coordinates = [(loc["latitude"], loc["longitude"]) for loc in self.locations]
        latitudes, longitudes = zip(*coordinates)
        center = (min(latitudes) + max(latitudes)) / 2, (min(longitudes) + max(longitudes)) / 2
        return center

    @property
    def data_pat_leaflet(self):
        data = {
            "fullscreencontrol": True,
            "zoomcontrol": True,
        }
        if self.context.initial_zoom_level:
            data["zoom"] = self.context.initial_zoom_level
            data["latitude"] = self.center[0]
            data["longitude"] = self.center[1]
        return json.dumps(data)

    @property
    def data_geojson(self):
        features = []
        for loc in self.locations:
            card_image = f"""<img src="{loc['lead_image_url']}" alt="picture">""" if loc["lead_image_url"] else ""
            card_title = f"""<h5>{loc['title']}</h5>"""
            card_text = f"""<p>{loc['description']}</p>""" if loc["description"] else ""
            popup = f"""<div>{card_image}<div>{card_title}{card_text}</div></div>"""
            features.append(
                {
                    "type": "Feature",
                    "properties": {"color": "blue", "popup": popup},
                    "geometry": {"type": "Point", "coordinates": [loc["longitude"], loc["latitude"]]},
                }
            )
        data = {"type": "FeatureCollection", "features": features}
        return json.dumps(data)

    @property
    @view.memoize
    def locations(self):
        brains = api.content.find(
            context=self.context,
            depth=1,
            portal_type="collective.contentsections.Location",
            sort_on="getObjPositionInParent",
        )
        results = [
            {
                "title": brain.Title,
                "description": brain.Description,
                "tags": brain.Subject,
                "latitude": brain.latitude,
                "longitude": brain.longitude,
                "lead_image_url": f"{brain.getURL()}/@@images/image/preview" if brain.image_scales else None,
            }
            for brain in brains
        ]
        return results
