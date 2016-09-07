#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#import webapp2 as usual, and cgi for escape_html method:
import webapp2
import re
import cgi

#define escape_html method:
def escape_html(s):
    return cgi.escape(s, quote = True)

form = """
<form method = "post">
    <h3> User Information </h3>

    <label> Username
    <input type = "text" name = "username" value = "%(unstr)s">
    </label>

    <div style="color: blue">%(errU)s</div><br>

    <label> Password
    <input type = "password" name = "password">
    </label>

    <div style="color: blue">%(errP)s</div><br>

    <label> Verify
    <input type = "password" name = "verify">
    </label>

    <div style="color: blue">%(errVP)s</div><br>

    <label> Email (optional)
    <input type = "text" name = "email" value = "%(emstr)s">
    </label>

    <div style="color: blue">%(errE)s</div><br>

    <input type = "submit"><br>

    <div style="color: blue">%(errAllU)s</div>
    <div style="color: blue">%(errAllP)s</div>
    <div style="color: blue">%(errAllE)s</div><br>
</form>
"""

# regex for username, password, and email validation:
# username:
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return USER_RE.match(username)

# password:
PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return PASS_RE.match(password)

# email:
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
def valid_email(email):
    return EMAIL_RE.match(email)


# input validation:
#validU = valid_username(self.request.get('username'))
#validP = valid_password(self.request.get('password'))
#validE = valid_email(self.request.get('email'))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        dictin = {"unstr" : "",
                  "emstr" : "",
                  "errU" : "",
                  "errP" : "",
                  "errVP" : "",
                  "errE" : "",
                  "errAllU" : "",
                  "errAllP" : "",
                  "errAllE" : ""}
        self.response.write(form % dictin)

        # input validation:
        validU = valid_username(self.request.get('username'))
        validP = valid_password(self.request.get('password'))
        validE = {valid_email(self.request.get('email')), ""}  ###### this allows any string without proper formatting
#        blankE = ""

        # if email is blank:
#        if self.request.get('email') == "":
#            blankE = ""
#        else: blankE = validE

    def error_check(self):
            # error key:
            UerrM = "Username not valid."
            PerrM = "Password not valid."
            VPerrM = "Passwords do not match."
            EmerrM = "Email not valid."
            AerrUM = "Valid usernames have 3 - 20 characters and no spaces."
            AerrPM = "Valid passwords have 3 - 20 characters."
            AerrEM = "Valid emails match this formatting: name@domain.com"

            # defaults error key:
            Noerr = ""

            # input validation:
            validU = valid_username(self.request.get('username'))
            validP = valid_password(self.request.get('password'))
            validE = {valid_email(self.request.get('email')), ""}
#            blankE = ""

        # if email is blank:
#        if self.request.get('email') == "":
#            blankE = ""
#        else: blankE = validE

            # error-checking for Username:
            if not validU: errU = UerrM
            else: errU = Noerr
            if not validU: errAllU = AerrUM
            else: errAllU = Noerr
#            if self.request.get('username') == "": errU = UerrM
#            else: errU = Noerr

            # error-checking for Password:
            if not validP: errP = PerrM
            else: errP = Noerr
            if not validP: errAllP = AerrPM
            else: errAllP = Noerr
#            if self.request.get('password') == "": errP = PerrM
#            else: errP = Noerr

            # error-checking for Verify:
            if not self.request.get('password') == self.request.get('verify'):
                errVP = VPerrM
            else: errVP = Noerr

            # error-checking for Email:
            if not validE: errE = EmerrM
            else: errE = Noerr
            if not validE: errAllE = AerrEM
            else: errAllE = Noerr

            # error-checking for blank Email, if blankE does not equal validE:



#            if blankE != validE: errE = Noerr
#            else: errE = Noerr
#            if blankE != validE: errAllE = Noerr
#            else: errAllE = Noerr

            # dict:
            dictout = {"unstr" : self.request.get('username'),
                       "emstr" : self.request.get('email'),
                       "errU" : errU,
                       "errP" : errP,
                       "errVP" : errVP,
                       "errE" : errE,
                       "errAllU" : errAllU,
                       "errAllP" : errAllP,
                       "errAllE" : errAllE}

            self.response.write(form % dictout)

    def post(self):

        # input validation:
        validU = valid_username(self.request.get('username'))
        validP = valid_password(self.request.get('password'))
        validE = {valid_email(self.request.get('email')), ""}

        # if email is blank:
#        if self.request.get('email') == "":
#            validE = ""
#        else:
#            validE = validE

#        if validE:
        if validU and validP and validE and self.request.get('password') == self.request.get('verify'):
            self.response.write("Welcome, " + self.request.get('username') + "!")

        else:
            self.error_check()

# error-checking
# for each error possibility, make if/else and for/while loop to check for errors:

 #if Uerror = False AND Perror = False AND Verror = False AND Emerror = False:
    # go to confirmation page

# if username == "": Uerror = True
    # else: Uerror = False
# if password == "": Perror = True
    # else: Perror = False
# if not verify == passord: Verror = True
    # else: Verror = False
# if not @ char in email: Emerror = True
    # else: Emerror = False

# 1) for any empty input except email
# 2) for usernames with spaces
# 3) for passwords less than 3 char
# 4) anything for emails? regex validation only (optional)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
