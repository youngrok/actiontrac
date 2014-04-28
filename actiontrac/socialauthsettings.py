AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.yahoo.YahooOpenId',
    'social.backends.amazon.AmazonOAuth2',
)
SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook', 'amazon')

SOCIAL_AUTH_AMAZON_KEY = 'amzn1.application-oa2-client.f366780f87ab4c7f9171c4194acf8c6a'
SOCIAL_AUTH_AMAZON_SECRET = 'b9c29dfcc016ba38d30e671a4921277682c4f2798ada4740ed099f6d87b4d19b'
SOCIAL_AUTH_FACEBOOK_KEY = '1390393911185605'
SOCIAL_AUTH_FACEBOOK_SECRET = '93260cd9295a85b9d7de65e760864ff6'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

#LOGIN_URL          = '/login-form/'
#LOGIN_REDIRECT_URL = '/'
#LOGIN_ERROR_URL    = '/login-error/'

#SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
#SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'unilogin.pipeline.update_profile',
    'social.pipeline.user.user_details'
)