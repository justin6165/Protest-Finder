from helper import *


def create_display_layout(img_link):
    pix = get_img(img_link)  # This is the image from each protest post
    pix = pix.scaled(256, 256, QtCore.Qt.KeepAspectRatio)
    display = QLabel()
    display.setPixmap(QPixmap(pix))  # Setting a QLabel to display the image

    img_layout = QVBoxLayout()  # This layout will hold the image from each protest post
    img_layout.setAlignment(Qt.AlignLeft)
    img_layout.setContentsMargins(0, 0, 0, 0)
    img_layout.addWidget(display)  # Add in image to layout

    return img_layout


def create_title_layout(title):
    title_label = QLabel(title)
    title_label.setMaximumWidth(250)

    title_layout = QVBoxLayout()
    title_layout.addWidget(title_label)

    return title_layout


def create_info_layout(date, descrip):
    info_date = QLabel(date)
    info_date.setMaximumWidth(250)
    info_descrip = QLabel(descrip)
    info_descrip.setMaximumWidth(250)
    info_descrip.setWordWrap(True)

    info_layout = QVBoxLayout()  # Displays title, date, description, etc, in a vertical format
    info_layout.addWidget(info_date)
    info_layout.addWidget(info_descrip)

    return info_layout


def create_link_layout(link):
    link_label = QLabel(link)

    link_layout = QVBoxLayout()
    link_layout.addWidget(link_label)

    return link_layout


def create_post_layout(post):
    # title, date, descrip, link, img_link = post

    title_layout = create_title_layout(post.title)
    img_layout = create_display_layout(post.img)
    info_layout = create_info_layout(post.date, post.description)
    link_layout = create_link_layout(post.link)

    body_layout = QHBoxLayout()
    body_layout.addLayout(img_layout)
    body_layout.addLayout(info_layout)

    post_layout = QVBoxLayout()  # The entire layout post is the image layout with the info layout
    post_layout.addLayout(title_layout)
    post_layout.addLayout(body_layout)
    post_layout.addLayout(link_layout)

    post_box = QGroupBox()
    post_box.setContentsMargins(0,0,0,0)
    post_box.setLayout(post_layout)

    return post_box

