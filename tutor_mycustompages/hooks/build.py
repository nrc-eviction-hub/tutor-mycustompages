from tutor import hooks

@hooks.Filters.IMAGE_BUILD_ARGS.register()
def build_args(args, context):
    # This tells Tutor to pip install your Django scaffold into LMS/CMS images
    args['PIP_EXTRA_REQUIREMENTS'] = 'git+https://github.com/nrc-eviction-hub/tutor-mycustompages.git@main'
    return args

