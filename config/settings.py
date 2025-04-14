# config/settings.py
#
# Configurações gerais do projeto

# URL base e de login (ajuste conforme necessário)
BASE_URL = "https://auth.iam.rio.cloud/"
LOGIN_URL = (
    "https://auth.iam.rio.cloud/login?post_login_redirect_uri="
    "https%3A%2F%2Fauth.iam.rio.cloud%2Foauth%2Fauthorize%3Fclient_id%3Dda6726bd-0ceb-4a59-964d-4d5ece2bf16a%26redirect_uri%3Dhttps%253A%252F%252Fhome.rio.cloud%252Fredirect%26response_type%3Dcode%26scope%3Dopenid%2Bprofile%2Bemail%2Bmenu.read%26state%3DSEU_STATE%26code_challenge%3DSUA_CODE_CHALLENGE%26code_challenge_method%3DS256"
)

# URLs das páginas a serem navegadas (exemplo para 6 páginas)
PAGE_URLS = {
    "pagina1": "https://home.rio.cloud/pagina1",
    "pagina2": "https://home.rio.cloud/pagina2",
    "pagina3": "https://home.rio.cloud/pagina3",
    "pagina4": "https://home.rio.cloud/pagina4",
    "pagina5": "https://home.rio.cloud/pagina5",
    "pagina6": "https://home.rio.cloud/pagina6",
}

# Formatos de data e hora
DATE_FORMAT = "%d/%m/%Y"
TIME_FORMAT = "%H:%M:%S"
