from pyramid.config import Configurator

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_route('dualrobot', '/')
    config.add_route('forward', '/forward')
    config.add_route('backward', '/backward')
    config.add_route('left', '/left')
    config.add_route('right', '/right')
    config.add_route('stop', '/stop')
    config.add_route('torvaldseye', '/torvaldson')
    config.add_route('torvaldsoff', '/torvaldsoff')
    config.add_route('directionone', '/directionone')
    config.add_route('directiontwo', '/directiontwo')
    config.add_route('directionthree', '/directionthree')
    config.add_route('directionfour', '/directionfour')
    config.add_route('stoptwo', '/stoptwo')
    config.add_route('linuseye', '/eyeon')
    config.add_route('linusoff', '/eyeoff')
    config.add_route('min', '/min')
    config.add_route('mid', '/mid')
    config.add_route('max', '/max')
    config.add_route('min2', '/min2')
    config.add_route('mid2', '/mid2')
    config.add_route('max2', '/max2')
    config.add_route('thirty', '/thirty')
    config.add_route('fifty', '/fifty')
    config.add_route('full', '/full')
    config.add_route('thirty2', '/thirty2')
    config.add_route('fifty2', '/fifty2')
    config.add_route('full2', '/full2')
    config.scan('.views')
    return config.make_wsgi_app()