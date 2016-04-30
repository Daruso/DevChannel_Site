# DevChannel_Site
A super secret repo for the DevChannel website

### Dependencies
  1. Python 3
  2. Flask
  3. Requests
  4. tinydb

### Installation
  * If you have conda installed: `conda env create -f environment.yml`.
  * If you have pip installed: `pip install -r requirements.txt`

Run `runserver.py` (`python3 runserver.py`). After that you can open the site:
  1. If you are on the host computer:  
    `localhost:3000`
  2. If you are on the same network as the host computer:  
    local-ip:3000 (e.g. `192.168.0.100:3000`)
  3. If you are on the other site of the planet:  
    public-ip:3000 (e.g. `60.60.60.60:3000`)
    This one probably requires port-forwarding too!

#### Database
To use this feature you have to be authenticated! Send your own cookie!
The server accepts 4 types of requests: GET, POST, PUT, DELETE
Every request call should specify at least 1 of the following parameters<sup>1</sup>:
  * slack_id
  * username
  * email

PUT accepts additional parameters (1 or more of the following):
  * langs
  * git
  * timezone
 ---
  * slack_id
  * username
  * email

1: slack_id is the primary key and should be prefered in all cases!

P.S: If you want to download the whole database you need a special parameter `req_all` set to `'true'`

#### Unittests
To run the tests: `python3 -m unittest discover tests`  
Do NOT merge a failing branch!
