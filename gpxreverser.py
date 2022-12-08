import gpxpy
import argparse
import os

parser = argparse.ArgumentParser(
    description='Script to reverse tracks in a GPX file')
parser.add_argument('--input', type=str, help='Source GPX file')
parser.add_argument('--output', type=str, help='Destination GPX file')
args = parser.parse_args()

if not os.path.exists(args.input):
    print("Error, source file not found")
else:
    gpx_file = open('test1.gpx', 'r')
    gpx = gpxpy.parse(gpx_file)

    myTracks = []
    for track in gpx.tracks:
        mySegments = []
        for segment in track.segments:
            myPoints = segment.points
            myPoints.reverse()
            mySegments.append(myPoints)
        myTracks.append(mySegments)

    reversedGPX = gpxpy.gpx.GPX()
    for track in myTracks:
        gpx_track = gpxpy.gpx.GPXTrack()
        reversedGPX.tracks.append(gpx_track)
        for segment in track:
            gpx_segment = gpxpy.gpx.GPXTrackSegment()
            gpx_track.segments.append(gpx_segment)
            gpx_segment.points = segment

    reversedXML = reversedGPX.to_xml()

    with open(args.output, "w") as f:
        f.write(reversedXML)
