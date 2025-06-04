<?php
session_start();
$config = include __DIR__ . '/config.php';

if (empty($_SESSION['authenticated'])) {
    header('Location: index.php');
    exit;
}

$maxSize = $config['max_size']();
$maxFiles = $config['max_files']();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $files = $_FILES['files'];
    if (count($files['name']) > $maxFiles) {
        die('Too many files uploaded');
    }

    for ($i = 0; $i < count($files['name']); $i++) {
        if ($files['error'][$i] !== UPLOAD_ERR_OK) {
            continue;
        }
        if ($files['size'][$i] > $maxSize) {
            continue;
        }
        $name = basename($files['name'][$i]);
        $type = mime_content_type($files['tmp_name'][$i]);
        if (preg_match('/pdf$/i', $type)) {
            $dir = $config['doc_dir'];
        } else {
            $dir = $config['image_dir'];
        }
        move_uploaded_file($files['tmp_name'][$i], $dir . $name);
    }
    header('Location: gallery.php');
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload Files</title>
</head>
<body>
<h1>Upload Files</h1>
<form method="post" enctype="multipart/form-data">
    <input type="hidden" name="MAX_FILE_SIZE" value="<?php echo $maxSize; ?>">
    <input type="hidden" name="MAX_FILE_COUNT" value="<?php echo $maxFiles; ?>">
    <input type="file" name="files[]" multiple required>
    <button type="submit">Upload</button>
</form>
</body>
</html>
