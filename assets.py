# from flask import current_app as app
from flask_assets import Bundle, Environment

def compile_stylesheet_bundles(assets: Environment) -> Environment:
    main_style_bundle = Bundle(
        'src/less/main.less',
        filters='cssmin',
        output='dist/css/main.min.css',
        extra={'rel': 'stylesheet/css'}  
    )
    assets.register('main_styles', main_style_bundle)

    # if app.config['ENVIRONMENT'] == 'development':
    main_style_bundle.build()

    return assets


def compile_js_bundles(assets: Environment) -> Environment:
    main_js_bundle = Bundle(
        'src/js/main.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )

    assets.register('main_js', main_js_bundle)

    main_js_bundle.build()

    return assets