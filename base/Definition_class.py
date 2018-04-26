import DM


class Definition:

    def __init__(self, settings={}):
        """Initialize a defiition given the settings dictionary"""
        self.settings = settings
        self.own_settings_dict = settings
        self.requiered_fields = list()
        self.default_settings = {}
        self.sanity_check_run = False
        self.sanity_check_ok_bool = False

    def get(self, name):
        """
        Get the value of a given setting and if it isn't explicitly set it will return the default
        """
        if name in self.settings:
            return self.settings[name]
        else:
            return self.get_default(name)

    def get_default(self, name):
        """
        Get the value of a default value for this type
            :param name: The setting-key
        """
        return self.default_settings.get(name, None)

    def set(self, name, value, override=True):
        """
        Set the value of a given setting.
            :param name: The name of the setting
            :param value: The value of the setting
            :param override: Wether or not to override a setting if it already exists
        """
        if name in self.settings and override:
            self.settings[name] = value
        elif name not in self.settings:
            self.settings[name] = value

    def load_settings(self, dict, override=False):
        """
        Load settings from the given dictionary.
            :param dict: The dictionary with settings to load
            :param override: Wether or not to override a setting if it already exists
        """
        if dict:
            for key, value in dict.items():
                self.set(key, value, override)
            for key, value in self.own_settings_dict.items():
                self.set(key, value, True)

    def load_defaults(self):
        for key, value in self.default_settings.items():
            self.set(key, value, False)

    def has(self, name):
        """Check if the given name is set in the setting dictionary."""
        return name in self.settings

    def __str__(self):
        re_string = ""
        for key, value in self.settings.items():
            re_string += "%-30s: %s\n" % (key, value)
        return re_string

    def register(self):
        """
        Will register the instances to the DM
        """
        DM.register(self)

    def load_inheritance(self):
        """
        Load all the settings from an inhetitance. This function is overidden by other classes.
        """
        pass

    def pre_sanity_check(self):
        """This is run before the sanity check. It is used to implement custom sanity-checking"""
        return list()

    def sanity_check(self):
        """Run a sanity-check and check that it has all the nessecary parameters set"""
        if self.sanity_check_run == False:
            error_list = list()
            error_list.extend(self.pre_sanity_check())
            if self.get("register") == 1:
                for field in self.requiered_fields:
                    if field not in self.settings:
                        error_list.append("'%s' is not set!" % field)
            self.error_list = error_list
            self.sanity_check_run = True
            if len(error_list) > 0:
                self.sanity_check_ok_bool = False
            else:
                self.sanity_check_ok_bool = True
        return self.error_list

    def sanity_check_ok(self):
        """Returns a True or False depending on the result of the sanity_check. Will return False if no sanity_check has been run"""
        if self.sanity_check_run == False:
            self.sanity_check()
        return self.sanity_check_ok_bool

    def set_requiered_field(self, field):
        """Register a field that is requiered for this definition"""
        self.requiered_fields.append(field)

    def set_default(self, key, value):
        """Add a default value to the register"""
        self.default_settings[key] = value

    def get_name(self):
        return self.__str__()
