import gettext
from schoolbot.helpers import config

el = gettext.translation('base', localedir='locales', languages=config["languages"])
el.install()
_ = el.gettext
