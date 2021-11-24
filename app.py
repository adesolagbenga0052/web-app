from flask import Flask, Request, redirect, flash
dataBank = None
def wait_app():
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')

    return app

half_app = wait_app()
 
def create_app(app):
    with app.app_context():
        from links import link as link_bp
        app.register_blueprint(link_bp)

    return app

if half_app.debug == True:
    from dbank import TEST_DATA_BANK
    dataBank = TEST_DATA_BANK()

if __name__ == "__main__":
    app = create_app(half_app)
    app.run()
