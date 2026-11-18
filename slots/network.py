def nonservice(offers,outages):
    availability = {}
    for outage in outages:
        affected = set(outage['paths'])
        availability[outage['id']] = sorted(row['id'] for row in offers if row['path'] in affected)
    return availability
