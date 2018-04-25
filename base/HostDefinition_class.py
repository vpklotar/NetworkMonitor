from base.Definition_class import Definition
import DM


class HostDefinition(Definition):
    """This contains all the nessecary information and functions for a host-definition"""

    def __init__(self, settings_dict):
        super().__init__(settings_dict)
        self.add_requiered_field('host_name')
        self.add_requiered_field('address')
        self.add_requiered_field('max_check_attempts')
        self.add_defaults()

    def add_defaults(self):
        self.add_default_value('check_period', '24x7')
        self.add_default_value('notification_interval', '60')
        self.add_default_value('notification_period', '24x7')
        self.add_default_value('contacts', '')
        self.add_default_value('contact_groups', 'admins')
        self.load_defaults()

    def load_inheritance(self):
        if self.has('use'):
            uses = self.get('use').split(',')
            for use in uses:
                use = use.strip()
                override = False
                if use.startswith('!'):
                    override = True
                    use = use[1:]
                self.load_settings(DM.filter(type='host', host_name=use).pop().settings, override)
