import logging
import os
import json

settings = {

    "settings": {


        # To be used by Flask: DEVELOPMENT ONLY
        "debug": True,

        # Flask host: DEVELOPMENT ONLY
        "host": "localhost",

        # Flask port: DEVELOPMENT ONLY
        "port": 5555,

        # Logging configurations
        "logging": {
            "level": logging.ERROR,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },

        # Email configurations
        "email": {
            "settings": "path_to_the_email.json",
            "user":  None,
            "password": None
        },

        # Folders
        "folders": {
            "config": "config/",
            "tmp": "tmp_path",
            "geoserver_datadir": "/home/vortex/programs/SERVERS/tomcat_geoservers/geoservers-test/data/",
            "distribution": "distribution_folder",
            "ftp": "ftp_folder"
        },

        # Geoserver
        "geoserver": {
            "geoserver_master": "http://168.202.28.214:10001/geoserver/rest",
            "geoserver_slaves": [],
            "username": "admin",
            "password": "geoserver",
        },

        # Metadata
        "metadata": {
            "url_create_metadata": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata",
            "url_get_metadata_uid": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata/uid/<uid>",
            "url_get_metadata": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/find"
        }
    }
}


# Setting email adderess from configuration file
def set_email_settings():
    if os.path.isfile(settings["settings"]["email"]["settings"]):
        settings["settings"]["email"] = json.loads(open(settings["settings"]["email"]["settings"]).read())
set_email_settings()