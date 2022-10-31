from webber.runner import AppRunner
from routes import routes


app = AppRunner(routes)
app.run()
