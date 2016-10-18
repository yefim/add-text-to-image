import os
from flask import Flask, request, send_file
from tempfile import NamedTemporaryFile
from urllib2 import urlopen
from wand.drawing import Drawing
from wand.image import Image


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET'])
def index():
    url = request.args['image']
    text = request.args['text']

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

        draw.font_size = 30
        draw.gravity = 'north_west'
        draw.text(0, 0, text)
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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
