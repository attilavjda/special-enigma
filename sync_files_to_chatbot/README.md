Sync Files to Chatbot
=====================

A Python script to monitor a directory for new files, upload them to a CustomGPT AI chatbot project, and periodically delete old files.

Features
--------

* Continuously monitors a specified directory for new files.
* Appends the current date to the filename and uploads it to the CustomGPT project.
* Periodically deletes files older than a set number of days (30 days by default) from the monitored directory.

Requirements
------------

* Python 3.6 or higher
* [CustomGPT-Client](https://github.com/customgpt/customgpt-client)
* [watchdog](https://github.com/gorakhargosh/watchdog)
* [schedule](https://github.com/dbader/schedule)

Setup
-----

1. Install the required libraries:

   ```
   pip install -r requirements.txt
   ```

2. Replace the placeholders in the script with the actual values relevant to your setup:

   * `API_TOKEN`: Your CustomGPT API token
   * `PROJECT_NAME`: The name of your CustomGPT project
   * `SITEMAP_PATH`: The sitemap path of your CustomGPT project
   * `WATCHED_FOLDER`: The folder you want to monitor for new files

3. Run the script:

   ```
   python sync_files_to_chatbot.py
   ```

   The script should be run in an environment that stays active, such as a server or a cloud-based service.

Contributing
------------

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Acknowledgments
---------------

* [CustomGPT-Client](https://github.com/customgpt/customgpt-client)
* [watchdog](https://github.com/gorakhargosh/watchdog)
* [schedule](https://github.com/dbader/schedule)