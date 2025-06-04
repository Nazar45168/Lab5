# PHP Upload and Gallery Template

This template demonstrates:

1. Multi-file uploads with size and count limits based on `php.ini`.
2. Counting images in the `uploads/imgs` directory and displaying only up to the limit.
3. Simple login protection with hashed password using `password_hash` and `password_verify`.
4. Uploading images and PDF documents. Images are displayed and documents are shown as links.

## Directory Structure

```
php-uploader/
│   config.php
│   index.php
│   login.php
│   upload.php
│   gallery.php
│   README.md
└───uploads/
    ├───imgs/    # uploaded images
    └───docs/    # uploaded documents
```

Place this folder on a PHP-enabled web server.
