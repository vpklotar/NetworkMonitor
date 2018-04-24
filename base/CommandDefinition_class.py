from base.Definition_class import Definition
import os.path
import SSE

class CommandDefinition(Definition):
    """This contains all the nessecary information and functions for a host-definition"""

    def __init__(self, settings_dict):
        super().__init__(settings_dict)
        self.add_requiered_field('command_name')
        self.add_requiered_field('command_line')
    
    def pre_sanity_check(self):
        return_list = list()
        if "command_line" in self.all_settings():
            self.set("command_line", SSE.substitue(self.get("command_line")))
            split_list = self.get('command_line').split(' ')
            if not os.path.isfile(split_list[0]):
                   return_list.append("File '%s' does not exist!" % split_list[0])         
        return return_list
    
    def get_name(self):
        return self.get('command_name')