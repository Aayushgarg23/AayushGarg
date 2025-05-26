# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email settings
#for sending mail to personal email along with admin
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'aayushgarg2003@gmail.com'  # Your Gmail address
EMAIL_HOST_PASSWORD = 'your-app-password'  # You'll need to generate this from Google Account
DEFAULT_FROM_EMAIL = 'aayushgarg2003@gmail.com'  # Your Gmail address
CONTACT_EMAIL = 'aayushgarg2003@gmail.com'  # Your Gmail address 
