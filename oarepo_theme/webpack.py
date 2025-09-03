from invenio_assets.webpack import WebpackThemeBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="oarepo",
    themes={
        "semantic-ui": {},
        "oarepo": {
            "entry": {},
            "dependencies": {},
            "devDependencies": {},
            "aliases": {
                "../../theme.config$": "less/theme.config",
                "../../less/site": "less/site",
                "../../less": "less",
                "@less": "less",
                "themes/oarepo": "less/oarepo",
            },
        }
    },
)