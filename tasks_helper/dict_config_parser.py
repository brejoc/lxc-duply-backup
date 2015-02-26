import ConfigParser

class DictConfigParser(ConfigParser.ConfigParser):
    """\
    Usage:
        parser = DictConfigParser()
        parser.read(path_to_ini_config)
        config_values = parser.as_dict()
    """

    def as_dict(self):
        """\
        Returns the settings from the ini config as dict.
        """
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d
