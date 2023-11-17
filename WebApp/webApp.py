import arrr
from pyscript import document


def generate_image(event):
    input_text = document.querySelector("#error_code")
    error_code = input_text.value
    error_img = "https://http.cat/" + error_code
    output_div = document.querySelector("#output")
    output_div.innerHTML = "<img src='" + error_img + "'/>"
