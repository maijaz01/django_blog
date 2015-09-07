import os
import pickle
import xml.etree.ElementTree as ET


class Permission(object):
    def read_file(self):
        """ This method will read file extention and call to respective method to get result
        """
        cur_dir = os.path.dirname(__file__)
        permissions_log = os.path.join(cur_dir, "permissions.xml")
        if permissions_log.split('.')[1]=='log':
            self.getLogFile(permissions_log)
        else:
            self.getXMLFile(permissions_log)

    def getLogFile(self, permissions_log):
        """This method convert pickle file and return dictionaries"""
        key_dict = {}
        if os.path.exists(permissions_log):
            fo = open(permissions_log,'U')
            file_log = pickle.load(fo)
            for key, value in file_log.items():
                if key[0] in key_dict.keys():
                    key_dict[key[0]].append({key[1]:[value]})
                else:
                    key_dict[key[0]] = [{key[1]:[value]}]
        print key_dict

    def getXMLFile(self, permissions_log):
        """This method read the xml file and convert into dictionaries
        """
        xml_dict = {}
        if os.path.exists(permissions_log):
            fo = open(permissions_log,'U')
            xml_obj = ET.parse(fo)
            root = xml_obj.getroot()
            for child in root:
                for item in child.findall("Item"):
                    if child.tag in xml_dict.keys():
                        xml_dict[child.tag].append({item.items()[1][1]:[item.text]})
                    else:
                        xml_dict[child.tag]=[{item.items()[1][1]:[item.text]}]
        print xml_dict

if __name__=="__main__":
    Permission=Permission()
    Permission.read_file()
