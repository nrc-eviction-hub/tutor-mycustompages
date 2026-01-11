from tutor import hooks

# Add mycustompages to LMS INSTALLED_APPS
hooks.Filters.ENV_PATCHES.add_item(
    (
        "lms-env",
        """
# MyCustomPages plugin
if "mycustompages" not in INSTALLED_APPS:
    INSTALLED_APPS.append("mycustompages")
"""
    )
)

# Optionally, you can add CMS env patches similarly:
# hooks.Filters.ENV_PATCHES.add_item(
#     (
#         "cms-env",
#         '''
# if "mycustompages" not in INSTALLED_APPS:
#     INSTALLED_APPS.append("mycustompages")
# '''
#     )
# )

