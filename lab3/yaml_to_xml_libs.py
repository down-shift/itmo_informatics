import xmltodict
import yaml
from yaml import SafeLoader


with open('lab3/d3210_schedule.yaml') as yaml_sch:
    json_data = yaml.load(yaml_sch, Loader=SafeLoader)
    xml_data = xmltodict.unparse(json_data['monday'])  # only one root is allowed
    print(xml_data)