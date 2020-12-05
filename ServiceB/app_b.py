from dapr.clients import DaprClient
from dapr.ext.grpc import App, InvokeServiceRequest, InvokeServiceResponse

app = App()


def get_client() -> DaprClient:
    return DaprClient()


def request_service_c():
    resp = get_client().invoke_service(
        id='python-service-c',
        method='hello',
        data=b'This is client b and request the service c.'
    )

    print(resp.content_type, flush=True)
    print(resp.text(), flush=True)


@app.method(name='hello')
def hello(request: InvokeServiceRequest) -> InvokeServiceResponse:
    print(request.data, flush=True)
    print(request.text(), flush=True)

    request_service_c()

    return InvokeServiceResponse(b'This is service b.Get the request from client a', "text/plain; charset=UTF-8")


app.run(9402)
