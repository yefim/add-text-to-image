Add Text to Image
==================

Pretty self-explanatory.

## API

````
GET /
````

With the following parameters:

| Parameter | Type   | Required? | Description |
|-----------|--------|-----------|-------------|
| `image`   | string | required  | The URL of the image that needs text added. |
| `text`    | string | required  | The text to add to the image. |
| `x`       | number | optional  | The x offset of the text from the left. Defaults to 0. |
| `y`       | number | optional  | The y offset of the text from the top. Defaults to 0. |
| `color`   | number | optional  | The text color. Defaults to #111111 (off-black). |
| `size`    | number | optional  | The font size of the text. Defaults to 30. |

## Contributors

* [Yefim Vedernikoff](https://twitter.com/yefim)
