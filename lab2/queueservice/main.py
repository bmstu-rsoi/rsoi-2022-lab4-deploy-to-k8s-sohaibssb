from quart import Quart
from queues.postcommandb import post_command_blueprint

app = Quart(__name__)
app.register_blueprint(post_command_blueprint)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8040)
