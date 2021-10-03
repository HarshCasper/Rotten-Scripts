import typing

import face_recognition
from PIL import Image, ImageFilter


def blur_human_faces(image_path: str) -> typing.Optional[Image.Image]:
    # Load the jpg file into a numpy array
    try:

        image = face_recognition.load_image_file(image_path)
    except FileNotFoundError:
        print("File not found")
        return

    # Find all the faces in the image
    face_locations = face_recognition.face_locations(image)

    # If there are no faces, return None
    if not face_locations:
        return

    # Create a PIL image from the numpy array
    img = Image.fromarray(image)

    # Create a mask for the face
    for face_location in face_locations:
        # Get the top, right, bottom, and left pixel locations
        top, right, bottom, left = face_location
        face_image = img.crop((left, top, right, bottom))
        face_image = face_image.filter(ImageFilter.GaussianBlur(radius=30))
        img.paste(face_image, (left, top, right, bottom))

    # Save the new image
    img.save("blurred_image.jpg")
    return img


if __name__ == "__main__":
    path = input("Enter path to the photo: ")
    print("Wait...")
    blur_human_faces(path)
    print("Done")
