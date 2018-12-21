whmcs-restful
==========================

This projects aims to provide an easy to use and consistent HTTP API of WHMCS software.

Installation
---------------------------
Very simple process::

  $ sudo pip install virtualenv
  $ cd /tmp/ && virtualenv test
  $ cd test && git clone git://github.com/riesal/whmcs-restful.git
  $ source bin/activate && pip install -r requirements.txt
  $ cd whmcs-restful
  $ python app.py
