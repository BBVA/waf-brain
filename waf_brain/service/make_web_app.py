from sanic import Sanic
from keras.models import load_model
from .end_points_waf import waf_blueprint
from .end_points_waf_simulator import waf_blueprint_simulator


def make_app(config_file: dict) -> Sanic:
    class _fake:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k.upper(), v)

    _A = _fake(**config_file)

    app = Sanic(__name__)
    app.config.from_object(_A)

    if app.config["ENABLE_TESTING"]:
        app.blueprint(waf_blueprint_simulator)
    else:
        app.blueprint(waf_blueprint)

    app.config["MODEL"] = load_model(config_file["model"])

    return app

