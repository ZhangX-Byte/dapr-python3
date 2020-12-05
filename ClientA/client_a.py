import time

from dapr.clients import DaprClient


def get_client() -> DaprClient:
    return DaprClient()


def call():
    while True:
        resp = get_client().invoke_service(
            id='python-service-b',
            method='hello',
            data=b'This is client a.',
            content_type='text/plain',
            metadata=(('header1', 'value1'),),
            http_verb='POST',
            http_querystring=(
                ('key1', 'value1'),),
        )

        # Print the response
        print(resp.content_type, flush=True)
        print(resp.text(), flush=True)

        time.sleep(2)


if __name__ == '__main__':
    call()
