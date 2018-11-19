from flask import Flask, request
from flask import render_template

from selenium import webdriver
from PIL import Image
import time
import base64

app = Flask(__name__)

@app.route('/')
def index():
    template = 'index.html'
    return render_template(template)

@app.route('/branding')
def branding():
    template = 'branding.html'
    return render_template(template)

@app.route('/test')
def test():
    template = 'test.html'
    return render_template(template)

@app.route('/chart', methods=['POST', 'GET'])
def chart():
    template = 'chart.html'
    driver = webdriver.Chrome()

    if request.method=='POST':

        title=request.form['title']
        link=request.form['url']
        source=request.form['source']
        path=request.form['path']

        driver.get('http://localhost:5000/branding')
        time.sleep(1)

        title_input = driver.find_element_by_id("change-title")
        link_input = driver.find_element_by_id("change-link")
        source_input = driver.find_element_by_id("change-source")
        path_input = driver.find_element_by_id("change-path")

        title_input.send_keys(title)
        time.sleep(0.1)
        link_input.send_keys(link)
        time.sleep(0.1)
        source_input.send_keys(source)
        time.sleep(0.1)
        path_input.send_keys(path)
        driver.find_element_by_id("submit-title").click()
        time.sleep(1)

        element = driver.find_element_by_id('viz')

        location = element.location
        size = element.size

        driver.save_screenshot(path + "shot.png")
        driver.quit()

        x = location['x']
        print(x)
        y = location['y']
        print(y)
        w = size['width']
        print(w)
        h = size['height']
        print(h)
        width = x + w
        height = y + h

        im = Image.open(path + 'shot.png')
        im = im.crop((int(x), int(y), int(width), int(height)))
        im.save(path + 'image.png')

        # image = request.files[path]
        #
        # image_64_encode = base64.encodestring(im)
        var_dict = {'screenshot': im}
        print(var_dict)


        # driver.quit()
        return 'Your chart is saved in ' + path
    else:
        return 'nothing'


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
