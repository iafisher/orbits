"""
MODEL 0 of the SOLAR SYSTEM

- The Solar System consists of two perfect spheres, the Sun and the Earth.
- The Earth moves around the Sun in a counterclockwise* circular orbit at a constant
  speed. One orbit takes exactly 365 days.
- The Sun does not move or rotate.
- The Earth does not rotate.

* Counterclockwise when viewed from above, i.e. from some point in the Solar System on
  the same side of the ecliptic as Earth's North Pole.


Two coordinate systems are defined, the solar coordinate system and the terrestrial coordinate system.  The SOLAR COORDINATE SYSTEM is a three-dimensional
Cartesian system for points in the Solar System.  The origin is defined to be the
position of the Sun's center.  The x- and y-axes lie on the ecliptic, such that at
time 0 the center of the Earth is located on the positive x-axis, and the Earth's orbit
passes through the positive y-axis before the negative y-axis.  The orientation of the
z-axis is defined by the right-hand rule.

Consider the position of Earth at time 0. There are two points on the Earth's surface
that are equally distant from the ecliptic, one with a positive z component and one with
a negative z component. Designate the point with a positive z component as the NORTH
POLE and the other point as the SOUTH POLE. Designate the great circle formed by the
intersection of Earth's surface with the ecliptic as the EQUATOR. Note that the Equator
divides Earth's surface into two hemispheres. Denote the hemisphere containing the North
Pole as the NORTHERN HEMISPHERE and the other hemisphere as the SOUTHERN HEMISPHERE. Now
consider the great circle defined by the intersection of Earth's surface with the xz
plane. Denote this great circle as the MERIDIAN CIRCLE. Like the Equator, the meridian
circle divides the Earth's surface into two hemispheres. Denote the hemisphere
containing only points with a negative y component as the WESTERN HEMISPHERE, and the
other hemisphere as the EASTERN HEMISPHERE. Notice that the meridian circle can be
divided into two half circles whose endpoints are the two poles. Denote the half circle
that is further from the origin as the PRIME MERIDIAN.

With these definitions, the TERRESTIAL COORDINATE SYSTEM can be defined as a
two-dimensional polar system for points on Earth's surface in which every point has a
latitude and longitude. The LATITUDE of a point p on Earth's surface is the angle
between the line from p to Earth's center and the line from the point on the Equator
nearest (in the solar coordinate system) to p. Negative latitudes denote points in the
Southern Hemisphere. The LONGITUDE of p is the angle between the line from p to Earth's
center and the line from the point on the Prime Meridian nearest to p. Negative
longitudes denote points in the Western Hemisphere.


Graphically, the Solar System appears as below at time 0 when viewed from above:

  |
  | +y
  |            <-- Earth's orbit
  |              .
  |                .
  |                 .
  |                  .             +x
 SUN ------------- EARTH <-.  --------
                           |
                           Prime Meridian


In the Python code, times are measured in seconds and distances are measured in meters.
Coordinates are represented at (x, y, z) tuples.
"""
import math

import common


EARTH_ORBIT_DURATION = 365*24*60
EARTH_ORBIT_RADIUS = 149600000*1000
EARTH_RADIUS = 6371*1000


def solar_system(t):
    """
    Return the state of the Solar System at time `t`.

    In this model, the Solar System's state is defined as the tuple

      (state of the Sun, state of Earth)
    """
    return (sun(t), earth(t))


def sun(t):
    """Return the position of the Sun's center at time `t`."""
    return (0, 0, 0)


def earth(t):
    """Return the position of Earth's center at time `t`."""
    theta = 2 * math.pi * (t / EARTH_ORBIT_DURATION)
    x, y = common.circle_xy(EARTH_ORBIT_RADIUS, theta)
    return (x, y, 0)


def terrestrial_to_solar_coordinate(t, lat, lon):
    """Convert the terrestrial coordinate at time `t` to a solar coordinate."""
    origin = earth(t)
    x, y = common.circle_xy(EARTH_RADIUS, common.longitude_to_radians(lon))
    z = _z_from_lat(lat)
    return (origin[0] + x, origin[1] + y, z)


def _z_from_lat(lat):
    return EARTH_RADIUS * math.sin(math.radians(lat))
