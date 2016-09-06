# signup.py
import webapp2
import cgi

<form method="post">
    Please enter user information.
    <br>

    <label> Username
        <input type="text" name="username">
    </label>

    <label> Password
        <input type="password" name="pwd">
    </label>

    <label> Verify Password
        <input type="password" name="pwd">
    </label>

    <label> Email Address (optional)
        <input type="text" name="email">
    </label>

    <br>
    <br>
    <input type="submit">
</form>


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):
        self.response.out.write("Thanks for your submission!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
