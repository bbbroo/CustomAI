from flask import Flask, render_template, request
import config
import views


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        if 'form1' in request.form:
            prompt = request.form['blogTopic']
            blogT = views.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.replace('\n', '<br>')

        if 'form2' in request.form:
            prompt = request.form['blogSection']
            blogT = views.generateBlogSections(prompt)
            blogSectionIdeas = blogT.replace('\n', '<br>')

        if 'form3' in request.form:
            prompt = request.form['blogExpander']
            blogT = views.blogSectionExpander(prompt)
            blogExpanded = blogT.replace('\n', '<br>')

        if 'form4' in request.form:
            prompt = request.form['blogTester']
            blogT = "The test was complete using {}".format(prompt)
            blogTested = blogT.replace('\n', '<br>')


    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8888', debug=True)
