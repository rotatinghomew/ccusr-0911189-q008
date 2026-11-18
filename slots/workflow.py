from .network import nonservice
from .population import estimates
from .purchases import spent


def report(data):
    return {'by_station':estimates(data['groups'],data['surveys']),
            'downtime':nonservice(data['offers'],data['outages']),
            'budget':spent(data['offers'],data['orders'],data['policy']['budget'])}
