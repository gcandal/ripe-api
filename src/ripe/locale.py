#!/usr/bin/python
# -*- coding: utf-8 -*-

class LocaleAPI(object):

    def locale_m(self, values, locale = "en-us"):
        url = self.base_url + "locale"
        contents = self.post(
            url,
            values = values,
            locale = locale
        )
        return contents

    def locale_s(self, value, locale = "en-us"):
        url = self.base_url + "locale" + "/" + value
        contents = self.post(
            url,
            locale = locale
        )
        return contents
