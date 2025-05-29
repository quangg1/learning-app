#** Security settings for all Content-Security-Policy (CSP) middleware
#* CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'", "*")
#* CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "stackpath.bootstrapcdn.com", "*")
#* CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'", "'unsafe-eval'", "ajax.cloudflare.com", "static.cloudflareinsights.com", "www.google-analytics.com", "ssl.google-analytics.com", "cdn.ampproject.org", "www.googletagservices.com", "pagead2.googlesyndication.com", "stackpath.bootstrapcdn.com", "*")
#* CSP_IMG_SRC = ("'self'", "www.google-analytics.com", "raw.githubusercontent.com", "googleads.g.doubleclick.net", "*")
#* CSP_FONT_SRC = ("'self'", "*")
#* CSP_CONNECT_SRC = ("'self'", "www.google-analytics.com", "*")
#* CSP_OBJECT_SRC = ("'self'", "*")
#* CSP_BASE_URI = ("'self'", "*")
#* CSP_FRAME_ANCESTORS = ("'self'", "*")
#* CSP_FORM_ACTION = ("'self'", "*")
#* CSP_INCLUDE_NONCE_IN = ('script-src', )
#* CSP_MANIFEST_SRC = ("'self'", "*")
#* CSP_WORKER_SRC = ("'self'", "*")
#* CSP_MEDIA_SRC = ("'self'", "*")

#** Private key for the CSP middleware
#* Security settings

from dev_core.settings.settings import DEBUG
import base64
import uuid

# Generate a random UUID
random_uuid = str(uuid.uuid4())

# Convert UUID to base64
nonce = base64.b64encode(random_uuid.encode()).decode()
#* https://developers.google.com/maps/documentation/javascript/content-security-policy?hl=vi
#* ----------------- CSP for development -----------------
CSP_DEFAULT_SRC = ("'self'",)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", f"'nonce-${nonce}'") if DEBUG else ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-eval'", f"'nonce-${nonce}'") if DEBUG else ("'self'",)
CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
CSP_IMG_SRC = ("'self'",)
#* ----------------- CSP for development -----------------
CSP_FONT_SRC = ("'self'",)
CSP_CONNECT_SRC = ("'self'",)
CSP_OBJECT_SRC = ("'none'",)
CSP_BASE_URI = ("'self'",)
CSP_FRAME_ANCESTORS = ("'none'",)
CSP_FORM_ACTION = ("'self'",)
CSP_INCLUDE_NONCE_IN = ('script-src', 'style-src', 'cdn.tailwindcss.com', 'cdnjs.cloudflare.com/ajax/libs/tailwindcss/4.0.0-alpha.11/lib.min.js')
CSP_MANIFEST_SRC = ("'self'",)
CSP_WORKER_SRC = ("'self'",)
CSP_MEDIA_SRC = ("'self'",)


# CSP_DEFAULT_SRC = ("'none'",)
# CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
# CSP_IMG_SRC = ("'self'",)