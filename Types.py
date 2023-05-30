
class WebPage:
    def __init__(self, url, html_content, name, **kwargs):
        self.url = url
        self.html_content = html_content
        self.name = name

        # Set user-defined attributes
        for attr_name, attr_value in kwargs.items():
            setattr(self, attr_name, attr_value)


    @staticmethod
    def pretty_print_html(html_content, indent_size=4, initial_indent=0):
        result = ""

        # Convert bytes to string

        decoded_content = html_content.decode('utf-8')

        for char in decoded_content:
            if char == '<':
                result += "\n" + " " * (indent_size * initial_indent) + char
                initial_indent += 1
            elif char == '>':
                result += char
                if initial_indent > 0:
                    initial_indent -= 1
            else:
                result += char

        print(result)


    def print_name(self):
        print("Page Name:", self.name)

    def print_url(self):
        print("Page URL:", self.url)

    def print_html(self):
        print("Page HTML:")
        self.pretty_print_html(self.html_content)


class NewsSite(WebPage):
    def __init__(self, url, html_content, name):
        super().__init__(url, html_content)
        self.name = name

    def print_name(self):
        print("News Site Name:", self.name)


class Store(WebPage):
    def __init__(self, url, html_content, name):
        super().__init__(url, html_content)
        self.name = name

    def print_name(self):
        print("Store Name:", self.name)