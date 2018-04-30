from base.Definition_class import Definition

class ServiceDefinition(Definition):
    def __init__(self, settings_dict):
        super().__init__(settings_dict)
        self.requieres_register_true = False
        self.set_requiered_field('host_name')
        self.set_requiered_field('check_command')
    
    def __str__(self):
        if self.sanity_check_ok() == True:
            return "%s@%s" % (self.get('check_command'), self.get('host_name'))
        else:
            return super().__str__()