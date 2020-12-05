from dapr.ext.grpc import App, InvokeServiceRequest, InvokeServiceResponse

app = App()


@app.method(name='hello')
def hello(request: InvokeServiceRequest) -> InvokeServiceResponse:
    print(request.metadata, flush=True)
    print(request.text(), flush=True)

    return InvokeServiceResponse(b'This is service c.And get the request from service b.', "text/plain; charset=UTF-8")


app.run(9401)
