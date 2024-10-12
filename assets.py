from flask import current_app as app
from flask_assets import Bundle, Environment

def compile_stylesheet_bundles(assets: Environment) -> Environment:
    main_style_bundle = Bundle(
        'src/less/main.less',
        filters='less,cssmin',
        output='dist/css/main.min.css',
        extra={'rel': 'stylesheet/css'}  
    )
    print(1)
    assets.register('main_styles', main_style_bundle)
    print(2)


    # if app.config['ENVIRONMENT'] == 'development':
    main_style_bundle.build()
    print(3)

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