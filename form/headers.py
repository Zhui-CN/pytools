from utils.headers import parse_headers


class HeadersForm:

    def __init__(self):
        self.headers_input.textChanged.connect(self.headers_parse)

    def headers_parse(self):
        input_text = self.headers_input.toPlainText().replace(":\n", ":")
        try:
            parse_text = parse_headers(input_text)
        except Exception as exc:
            parse_text = str(exc)
        self.headers_output.setPlainText(parse_text)
