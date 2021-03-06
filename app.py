import os
from flask import Flask, request, send_file
from tempfile import NamedTemporaryFile
from urllib2 import urlopen
from wand.drawing import Drawing
from wand.image import Image
from wand.color import Color


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET'])
def index():
    url = request.args['image']
    text = request.args['text']
    x = request.args.get('x', 0, type=int)
    y = request.args.get('y', 0, type=int)
    color = request.args.get('color', '#111111')
    size = request.args.get('size', 30, type=int)

    with Drawing() as draw:
        """
        font
        font_family
        font_resolution
        font_size
        font_stretch
        font_style
        font_weight
        gravity
        text_alignment
        text_antialias
        text_decoration
        text_direction
        text_interline_spacing
        text_interword_spacing
        text_kerning
        text_under_color
        """

        draw.font_family = 'Helvetica'
        draw.font_size = size
        draw.fill_color = Color(color)
        draw.gravity = 'north_west'
        draw.text(x, y, text)
        response = urlopen(url)

        try:
            with Image(file=response) as img:
                draw(img)
                temp_file = NamedTemporaryFile(mode='w+b', suffix=img.format)
                img.save(file=temp_file)
                temp_file.seek(0, 0)
                return send_file(temp_file, mimetype=img.mimetype)
        finally:
            response.close()


@app.errorhandler(400)
def bad_request(error):
    return send_file('placeholder.png')


@app.errorhandler(500)
def server_error(error):
    return send_file('placeholder.png')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
