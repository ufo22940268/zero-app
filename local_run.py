from zero import client

app = client.create_app()
app.run(port=10000, debug=True)
