# signup start-over

import webapp2

form = """
<form method = "post">
    <input type = "text" name = "unstr" value = "username">
    <input type = "text" name = "password">
    <input type = "text" name = "verify">
    <input type = "text" name = "emstr" value = "email">
    <input type = "text" name = "erstr" value = "error">
    <input type = "submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self):
        #v1 = self.request.get('confusing')
        #v2 = self.request.get('grins')
        self.response.write(self.request.get('username')
                            + self.request.get('email')
                            + self.request.get('error'))
        #self.response.write('Goodbye world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


# other old drafts:

#define form format:
form="""
<form method="post">
    <h3> User Information </h3>

    <label> Username
        <input type="text" name="username" value= "%(unstr)s">
    </label>
    <br>

    <label> Password
        <input type="password" name="pwd">
    </label>
    <br>

    <label> Verify Password
        <input type="password" name="vpwd">
    </label>
    <br>

    <label> Email Address (optional)
        <input type="text" name="email" value="%(emstr)s">
    </label>
    <br>

    <div style="color: blue">%(erstr)s</div>
    <br>
    <br>
    <input type="submit">
</form>
"""

# codeacadem example1 str subst:
#string_1 = "Camelot"
#string_2 = "place"
#print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

#unstr = "username"
#emstr = "email"
#erstr = "error"
#print "User %s and %s here, and if they do not exist, print %s" % (unstr, emstr, erstr)

# example2:
#name = raw_input("What is your name?")
#quest = raw_input("What is your quest?")
#color = raw_input("What is your favorite color?")
#print "Ah, so your name is %s, your quest is %s, " \
#"and your favorite color is %s." % (name, quest, color)

#***********
#username =

#def valid_username(username):
#        if(username):
#                username = username.capitalize()
#        if(username in usernames):
#                return username


#dict = {"unstr": escape_html(username),
    #   "password": escape_html(password),
    #   "verify": escape_html(verify),
#        "emstr": escape_html(email)
#        "erstr": escape_html(error)}

class MainPage(webapp2.RequestHandler):
    #define above variables with escape_html method:
    #unstr = "unstr" : escape_html(username)
    #emstr = "email" : escape_html(email)
    #erstr = "error" : escape_html(error)
    #def write_form(self, username="", email="")
        #print "User %s and %s here" % (username, email)
    #   self.response.write(form % {"username": escape_html(unstr)})


    #define write_form method with blank starting defaults:
    #def write_form(self, username="", email="", error=""):
    #def write_form(self, username="", email=""):
                    # Go to form string and sub that user input for this first variable : escaped version
                    # key-value pairs listed - look up key (like an index) and get value printed
        #self.response.write(form % {"unstr": escape_html(username),
        #                            "erstr": escape_html(error),
                        #            "password": escape_html(password),
                        #            "verify": escape_html(verify),
        #                            "emstr": escape_html(email)})

    #def get(self, username="", email=""):
    #    self.response.write(form % {unstr, emstr})
#    dict = {"unstr": escape_html(username),
        #   "password": escape_html(password),
        #   "verify": escape_html(verify),
#            "emstr": escape_html(email)
#            "erstr": escape_html(error)}

    #v1 = self.request.get('unstr')
    #v2 = self.request.get('emstr')
    #v3 = self.request.get('erstr')
    #self.response.write(v1)

    def get(self):
        #use above write_form method with blank defaults for inputs:
        #self.write_form()
        self.response.write(form)

    def post(self):
        #rewrite form, but with preserved user's username and email

        #if you use write_form(), without IDed params, you'll only reload the form with param defaults:
        self.response.write(form % dict)
        #self.write_form("unstr", "emstr") # remember to add error as param when you address them
        #self.write_form(form % dict)
        #if you use .response.write(form), you'll reload the form with %stringSub format only:
        #self.response.write(form)

        #fetch user's input and check for errors:
        #user_username = self.request.get('username')

        #user_pwd = valid_pwd(self.request.get('pwd'))
        #user_vpwd = valid_vpwd(self.request.get('vpwd'))
        #user_email = valid_email(self.request.get('email'))

        #username = valid_username(user_username)

        ### if error, send error; if no error, send confirmation:
    #    if not (user_username and user_pwd and user_email):
    #        self.write_form("That doesn't look right.")
    #    else:
    #        self.redirect("/Thanks!")

        #self.response.write("Thanks")


#usual footer to ID webapp2 and debugger:
app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
