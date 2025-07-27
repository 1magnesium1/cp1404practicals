from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """ Simple app to dynamically create labels for each name """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Franco", "Brock", "Ryan", "Douglas", "Elizabeth"]

    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            label = self.create_label(name)
            self.root.ids.labels_box.add_widget(label)
        return self.root

    def create_label(self, name):
        label = Label(text=name)
        return label


DynamicLabelsApp().run()
