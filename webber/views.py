

class TemplateView:
    def __init__(self, template_name):
        self.template_name = template_name

    def to_html(self) -> str:
        try:
            with open(self.template_name, "r") as f:
                self.data = f.read()
            return self.data
        except:
            print('[31m', f"[WebberError] ---> {self.template_name} nomli fayl topilmadi.")
            return f"<center><b>Webber FileNotFoundError</b></center><code>{self.template_name} topilmadi.</code>"

