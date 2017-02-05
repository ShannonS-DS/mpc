# Copy this file into secrets.py and set keys, secrets and scopes.

# Details of your community
community = {
	'name': 'Luther College',
	'address': '700 College Drive Decorag, IA',
	'lat': 43.313059,
	'lng': -91.799501
}

# This is a session secret key used by webapp2 framework.
# Get 'a random and long string' from here:
# http://clsc.net/tools/random-string-generator.php
# or execute this from a python shell: import os; os.urandom(64)
SESSION_KEY = "\xa6EE\x01\x83\xa4\xcb\x87\x89\x81\xf0\xec\xe4'\x89=\xdc\x1a\xc1\xd1q\x9f \x1dt\xad\xfdY\x08]\x94\xf3N|\x83\x11^@v\xae\x98\t\xf5\xefB\xa8\\\xbce\x89\noGH\xb3>A\\\x9dvN\xd9\xa5K"

# Google APIs
GOOGLE_APP_ID ='400916539476-e6i1tbkpsf6s3vc6p08tmce3lsfu37sk.apps.googleusercontent.com'
GOOGLE_APP_SECRET ='LGGdfAkj1OKT5_aQ7oGTJ14d'

# Facebook auth apis
FACEBOOK_APP_ID = '631641680299721'
FACEBOOK_APP_SECRET = '5c0bcf44f37b53299855cf815a6e54266'

# https://dev.twitter.com/apps
TWITTER_CONSUMER_KEY = 'LeQDWs29fMENzxtGcmTA6cC5Y'
TWITTER_CONSUMER_SECRET = 'sb6pfGFTiew8MidvWo2rtuhJJ7S1Qk89mYGyVV97PdckarLQmR'


# config that summarizes the above
# do not modify the following
AUTH_CONFIG = {
  # OAuth 2.0 providers
  'google'      : (GOOGLE_APP_ID, GOOGLE_APP_SECRET,
                  'https://www.googleapis.com/auth/userinfo.profile'),

  'facebook'    : (FACEBOOK_APP_ID, FACEBOOK_APP_SECRET,
                  'user_about_me'),

  # OAuth 1.0 providers don't have scopes
  'twitter'     : (TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)

  # OpenID doesn't need any key/secret
}
