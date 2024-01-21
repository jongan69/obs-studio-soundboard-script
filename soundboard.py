import obspython as S


class Hotkey:
    def __init__(self, callback, obs_settings, _id):
        self.obs_data = obs_settings
        self.hotkey_id = S.OBS_INVALID_HOTKEY_ID
        self.hotkey_saved_key = None
        self.callback = callback
        self._id = _id

        self.load_hotkey()
        self.register_hotkey()
        self.save_hotkey()

    def register_hotkey(self):
        description = "Soundboard " + str(self._id)
        self.hotkey_id = S.obs_hotkey_register_frontend(
            "htk_id" + str(self._id), description, self.callback
        )
        S.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)

    def load_hotkey(self):
        self.hotkey_saved_key = S.obs_data_get_array(
            self.obs_data, "htk_id" + str(self._id)
        )
        S.obs_data_array_release(self.hotkey_saved_key)

    def save_hotkey(self):
        self.hotkey_saved_key = S.obs_hotkey_save(self.hotkey_id)
        S.obs_data_set_array(
            self.obs_data, "htk_id" + str(self._id), self.hotkey_saved_key
        )
        S.obs_data_array_release(self.hotkey_saved_key)


class h:
    htk_copy = None  # this attribute will hold instance of Hotkey
    outputIndex = 63  # Last index


# Description displayed in the Scripts dialog window
def script_description():
  return """OBS Soundboard!
            Included Sounds: bruh
            Set your hotkeys and spam the keys."""

def cb1(pressed):
    if pressed:
        print("Playing Sound" + e1.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e1.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource


def cb2(pressed):
    if pressed:
        print("Playing Sound" + e2.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e2.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource

def cb3(pressed):
    if pressed:
        print("Playing Sound" + e3.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e3.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource

def cb4(pressed):
    if pressed:
        print("Playing Sound" + e4.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e4.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource

def cb5(pressed):
    if pressed:
        print("Playing Sound" + e5.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e5.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource

def cb6(pressed):
    if pressed:
        print("Playing Sound" + e6.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e6.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource

def cb7(pressed):
    if pressed:
        print("Playing Sound" + e7.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e7.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource

def cb8(pressed):
    if pressed:
        print("Playing Sound" + e8.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e8.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource

def cb9(pressed):
    if pressed:
        print("Playing Sound" + e9.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e9.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource

def cb10(pressed):
    if pressed:
        print("Playing Sound" + e10.txt)
        outputIndex = 63  # Last index

        mediaSource = S.obs_source_create_private(
            "ffmpeg_source", "Global Media Source", None
        )
        s = S.obs_data_create()
        S.obs_data_set_string(s, "local_file", script_path() + e10.txt)
        S.obs_source_update(mediaSource, s)
        S.obs_source_set_monitoring_type(
            mediaSource, S.OBS_MONITORING_TYPE_MONITOR_AND_OUTPUT
        )
        S.obs_data_release(s)

        S.obs_set_output_source(outputIndex, mediaSource)
        return mediaSource


class e:
    txt = "default txt"


e1 = e()
e2 = e()
e3 = e()
e4 = e()
e5 = e()
e6 = e()
e7 = e()
e8 = e()
e9 = e()
e10 = e()

h1 = h()
h2 = h()
h3 = h()
h4 = h()
h5 = h()
h6 = h()
h7 = h()
h8 = h()
h9 = h()
h10 = h()


def script_properties():
    props = S.obs_properties_create()
    # S.obs_properties_add_text(props, "_text1", "_text1:", S.OBS_TEXT_DEFAULT)
    # S.obs_properties_add_text(props, "_text2", "_text2:", S.OBS_TEXT_DEFAULT)
    return props


# def script_update(settings):
#     # _text1 = S.obs_data_get_string(settings, "_text1")
#     # _text2 = S.obs_data_get_string(settings, "_text2")
#     e1.txt = "bruh.mp3"
#     e2.txt = "bugatti.mp3"
#     e3.txt = "chad.mp3"
#     e4.txt = "huh.mp3"
#     e5.txt = "saul.mp3"
#     e6.txt = "sigma.mp3"
#     e7.txt = "two.mp3"
#     e8.txt = "vine.mp3"
#     e9.txt = "why.mp3"
#     e10.txt = "windows.mp3"


def script_load(settings):
    e1.txt = "bruh.mp3"
    e2.txt = "bugatti.mp3"
    e3.txt = "chad.mp3"
    e4.txt = "huh.mp3"
    e5.txt = "saul.mp3"
    e6.txt = "sigma.mp3"
    e7.txt = "two.mp3"
    e8.txt = "vine.mp3"
    e9.txt = "why.mp3"
    e10.txt = "windows.mp3"
    h1.htk_copy = Hotkey(cb1, settings, "Button 1: " + e1.txt)
    h2.htk_copy = Hotkey(cb2, settings, "Button 2: " + e2.txt)
    h3.htk_copy = Hotkey(cb3, settings, "Button 3: " + e3.txt)
    h4.htk_copy = Hotkey(cb4, settings, "Button 4: " + e4.txt)
    h5.htk_copy = Hotkey(cb5, settings, "Button 5: " + e5.txt)
    h6.htk_copy = Hotkey(cb6, settings, "Button 6: " + e6.txt)
    h7.htk_copy = Hotkey(cb7, settings, "Button 7: " + e7.txt)
    h8.htk_copy = Hotkey(cb8, settings, "Button 8: " + e8.txt)
    h9.htk_copy = Hotkey(cb9, settings, "Button 9: " + e9.txt) 
    h10.htk_copy = Hotkey(cb10, settings, "Button 10: " + e10.txt)

def script_save(settings):
    h1.htk_copy.save_hotkey()
    h2.htk_copy.save_hotkey()
    h3.htk_copy.save_hotkey()
    h4.htk_copy.save_hotkey()
    h5.htk_copy.save_hotkey()
    h6.htk_copy.save_hotkey()
    h7.htk_copy.save_hotkey()
    h8.htk_copy.save_hotkey()
    h9.htk_copy.save_hotkey()
    h10.htk_copy.save_hotkey()