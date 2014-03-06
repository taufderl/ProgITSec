def retKML(ip):
    rec = gi.record_by_name(ip)
    try:
	longitude = rec['longitude']
	latitude = rec['latitude']
	kml = (
	'<Placemark>\n'
	'<name>%s</name>\n'
	'<Point>\n'
	'<coordinates>%6f,%6f</coordinates>\n'
	'</Point>\n'
	'</Placemark>\n'
	)%(ip,longitude, latitude)
	return kml
    except Exception, e:
	return ''