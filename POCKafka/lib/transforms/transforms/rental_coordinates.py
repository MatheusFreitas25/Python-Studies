from shapely import wkb, geometry
from datetime import datetime
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def validate_latlong(arg):
    return (
        arg
        if len(arg) > 0 and -90 <= arg[0] <= 90 and -180 <= arg[1] <= 180
        else []
    )


def split_arg(arg, value):
    return list(map(float, arg.split(value))) if isinstance(arg, str) else arg


def invert_position(points):
    new_points = []
    for x in range(0, len(points) - 1):
        new_points.append((points[x][1], points[x][0]))
    return geometry.Polygon(new_points).wkt


def get_latlong(record, key):
    try:
        latlong = split_arg(record[key], ",")
    except:
        latlong = []
        if record[key] is not None and record[key] != "":
            hex_location = record[key][10:]
            point = wkb.loads(
                hex_location,
                hex=True,
            )
            try:
                latlong.append(point.x)
                latlong.append(point.y)
            except:
                return [invert_position(list(point.exterior.coords))]

    return validate_latlong(latlong)


def parse_record(record: dict, fields_to_transform):
    for key in list(record.keys()):
        lat_long = (
            get_latlong(record, key) if key in fields_to_transform else []
        )

        if len(lat_long) > 1:
            record["latitude"] = float(lat_long[0])
            record["longitude"] = float(lat_long[1])

            record.pop(key)
        elif len(lat_long) == 1 and key in fields_to_transform:
            record[key] = lat_long[0]

    return record


def format_coordinates_records(records, fields_to_transform):
    return [parse_record(record, fields_to_transform) for record in records]
