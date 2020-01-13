
import configparser



class Configuration(object):
    __instance = None

    '''
    Public Implementation
    '''
    @staticmethod
    def get_instance():
        """ Static access method. """
        if Configuration.__instance is None:
            Configuration()

        return Configuration.__instance

    def get(self, section, option):
        try:
            return self.config.get(section, option)
        except Exception:
            pass

        return None

    def get_section(self, section):
        values = {}
        for key in self.config.options(section):
            value = self.get(section, key)
            if value.lower() in ('true', '1', 'yes'):
                values[key] = True

            elif value.lower == ('false', '0', 'no'):
                values[key] = False

            else:
                values[key] = self.get(section, key)

        return values

    def platform_type(self):
        platform = self.get("general", "platform")

        if platform.lower() == "ios":
            return PlatformType.IOS

        if platform.lower() == "android":
            return PlatformType.ANDROID

        if platform.lower() == "apple_tv":
            return PlatformType.APPLE_TV

        if platform.lower() == "android_tv":
            return PlatformType.ANDROID_TV

        if platform.lower() == "samsung_tv":
            return PlatformType.SAMSUNG_TV

    def is_mobile_platform(self):
        return self.platform_type() in [PlatformType.ANDROID, PlatformType.IOS]

    def is_tv_platform(self):
        return self.platform_type() in [PlatformType.APPLE_TV, PlatformType.SAMSUNG_TV, PlatformType.ANDROID_TV]

    def is_selenium_based_test(self):
        return self.platform_type() in [PlatformType.SAMSUNG_TV]

    def is_appium_based_test(self):
        return self.platform_type() in [PlatformType.IOS, PlatformType.ANDROID, PlatformType.ANDROID_TV]

    def get_bundle_id(self):
        platform = self.platform_type()

        if platform == PlatformType.IOS:
            return self.get("appium", "bundleId")

        if platform == PlatformType.ANDROID or platform == PlatformType.ANDROID_TV:
            return self.get("appium", "appPackage")

        if platform == PlatformType.SAMSUNG_TV:
            return self.get("general", "bundle_id")

    def add_custom_configuration(self, config):
        if config is not None:
            for section in config:
                for option in config[section]:
                    if section == 'appium' and option == 'layout_id':
                        self.__add_layout_id__(config[section][option])
                    else:
                        self.config.set(section, option, config[section][option])
    '''
    Private Implementation
    '''
    def __init__(self):
        """ Virtually private constructor. """
        if Configuration.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Configuration.__instance = self
            self.load_configuration_files()

    def __add_layout_id__(self, layout_id):
        url_scheme = '-d %s://present?rivers_configuration_id=%s' % (self.get_bundle_id(), layout_id)
        self.config.set('appium', 'optionalIntentArguments', url_scheme)

    def load_configuration_files(self):
        self.config = configparser.ConfigParser()
        self.config.optionxform = str
        self.config.read(PTAH_PROJECT_ABSOLUTE_PATH + "/config.cfg")
