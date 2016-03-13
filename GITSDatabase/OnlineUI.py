'''
@author: Michael Jannain

This uses Jinja2 to create the online facing portion of our GITS database.
'''

# -*- coding: utf-8 -*-

import jinja2
import os


def printHTMLEnvironment(html_environment):
    print html_environment


def createEnvironment(directory):
    return jinja2.Environment(autoescape=False,
        loader=jinja2.FileSystemLoader(os.path.join(directory, "Jinja_Templates")), trim_blocks=False)


def renderHTML(template_environment, template_filename, context):
    return template_environment.get_template(template_filename).render(context)


def createIndexHTML():
    THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_ENVIRONMENT = createEnvironment(THIS_DIRECTORY)

    #print "\nThis Directory: " + THIS_DIRECTORY + "\n"
    #printHTMLEnvironment(TEMPLATE_ENVIRONMENT)

    output_filename = "output.html"
    template_filename = "online_template.html"
    urls = ["http://www.gitsdatabase.com/"]
    context = {'urls': urls}
    with open(output_filename, "w") as f:
        html = renderHTML(TEMPLATE_ENVIRONMENT, template_filename, context)
        f.write(html)
    print "Output file 'output_html' created in workspace...\n"


def main():
    createIndexHTML()


if __name__ == "__main__":
    print "\n######################################################################################"
    print "Project: GITS Database"
    print "######################################################################################\n"
    main()

'''
t = jinja2.Template("Hello {{ something }}!")
output = t.render(something="World")
print output
'''

'''
THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_ENVIRONMENT = jinja2.Environment(autoescape=False, loader=jinja2.FileSystemLoader(
    os.path.join(THIS_DIRECTORY, "Jinja_Templates")), trim_blocks=False)
print TEMPLATE_ENVIRONMENT.get_template("online_template.html").render(title="GITS Database")


def printHTMLDoc():
    TEMPLATE_ENVIRONMENT = jinja2.Environment(autoescape=False, loader=jinja2.FileSystemLoader(os.path.join
        (THIS_DIRECTORY, "Jinja_Templates")), trim_blocks=False)
    print TEMPLATE_ENVIRONMENT.get_template("online_template.html").render(title="GITS Database")
'''

'''
THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_ENVIRONMENT = jinja2.Environment(autoescape=False, loader=jinja2.FileSystemLoader(
    os.path.join(THIS_DIRECTORY, "Jinja_Templates")), trim_blocks=False)
print TEMPLATE_ENVIRONMENT.get_template("online_template.html").render(title="GITS Database")
'''
