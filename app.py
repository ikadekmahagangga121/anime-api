from flask import Flask, jsonify, send_from_directory
import os
import json

app = Flask(__name__)
anime_images_dir = "static/anime_images"

# Baca data gambar dari JSON
with open('anime_data.json', 'r') as json_file:
    anime_data = json.load(json_file)

@app.route('/anime_images/<int:image_id>')
def get_anime_image(image_id):
    # Temukan data gambar berdasarkan ID
    for image in anime_data['images']:
        if image['id'] == image_id:
            filename = image['filename']
            return send_from_directory(anime_images_dir, filename)

@app.route('/anime_images')
def get_all_anime_images():
    # Mengembalikan daftar semua gambar anime
    return jsonify(anime_data['images'])

if __name__ == '__main__':
    app.run(debug=True)
