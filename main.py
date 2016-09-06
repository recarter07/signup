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
import cgi

#define escape_html method:
def escape_html(s):
    return cgi.escape(s, quote = True)

form = """
<form method = "post">
    <h3> User Information </h3>

    <label> Username
    <input type = "text" name = "username" value = "%(unstr)s"><br>
    </label>

    <label> Password </h3>
    <input type = "password" name = "password"><br>
    </label>

    <label> Verify </h3>
    <input type = "password" name = "verify"><br>
    </label>

    <label> Email (optional) </h3>
    <input type = "text" name = "email" value = "%(emstr)s"><br>
    </label>

    <div style="color: blue">error</div><br>
    <input type = "submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        dictin = {"unstr" : "", "emstr" : ""}
        self.response.write(form % dictin)

    def post(self):
        dictout = {"unstr" : self.request.get('username'),
                   "emstr" : self.request.get('email')}
        self.response.write(form % dictout)
#
# if all checks out, no errors, move to new page:
#    def post(self):
#        self.response.write("Thank you!")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
