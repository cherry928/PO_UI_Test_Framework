import os
import yaml

current_path = os.path.dirname(__file__)
yaml_path = os.path.join(current_path, '../page_element/login_page.yaml')


class ReadYaml:
    def __init__(self, path=yaml_path):
        self.path = path
    def read_yaml(self):
        pageElements = {}
        with open(self.path, 'r', encoding='utf-8') as yamlfile:
            page = yaml.load(yamlfile, Loader=yaml.FullLoader)
            pageElements.update(page)
        return pageElements

if __name__=='__main__':
    readyaml = ReadYaml()
    elements = readyaml.read_yaml()
    print(elements)