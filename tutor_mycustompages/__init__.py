from tutor import hooks

# Add mycustompages to LMS Django settings
hooks.Filters.APP_SETTINGS.add_item(
    (
        "lms",
        {
            "INSTALLED_APPS": ["mycustompages"],
        },
    )
)

