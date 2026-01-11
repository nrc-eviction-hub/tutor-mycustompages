from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "lms-env",
        "common",
        """
        INSTALLED_APPS.append("mycustompages")
        """
    )
)

