import APJP

APJP.APJP.APJP_KEY = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[0] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[0] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[1] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[1] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[2] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[2] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[3] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[3] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_KEY[4] = ''
APJP.APJP.APJP_REMOTE_HTTP_SERVER_RESPONSE_PROPERTY_VALUE[4] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[0] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[0] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[1] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[1] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[2] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[2] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[3] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[3] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_KEY[4] = ''
APJP.APJP.APJP_REMOTE_HTTPS_SERVER_RESPONSE_PROPERTY_VALUE[4] = ''

from bae.core.wsgi import WSGIApplication

application = WSGIApplication( APJP.Application() )
