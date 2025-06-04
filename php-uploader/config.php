<?php
// Simple configuration for upload system
return [
    'users' => [
        // userid => password_hash
        'admin' => password_hash('secret', PASSWORD_DEFAULT),
    ],
    'image_dir' => __DIR__ . '/uploads/imgs/',
    'doc_dir'   => __DIR__ . '/uploads/docs/',
    // Maximum size for uploaded files (bytes) from php.ini
    'max_size' => function () {
        $val = ini_get('upload_max_filesize');
        return parse_size($val);
    },
    // Maximum number of files allowed from php.ini
    'max_files' => function () {
        return (int) ini_get('max_file_uploads');
    },
];

function parse_size($size)
{
    $unit = strtolower(substr($size, -1));
    $bytes = (int) $size;
    switch ($unit) {
        case 'g':
            $bytes *= 1024;
        case 'm':
            $bytes *= 1024;
        case 'k':
            $bytes *= 1024;
    }
    return $bytes;
}
