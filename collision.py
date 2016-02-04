def circleCircle(circle1, circle2):
    '''Two circles intersect when the distance between radii is less than the sum of the radii.'''
    d = circle1.position - circle2.position
    distance = d.magnitudeSquared()
    radii = (circle1.radius + circle2.radius)**2
    return distance <= radii

