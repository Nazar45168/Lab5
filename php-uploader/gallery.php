<?php
session_start();
$config = include __DIR__ . '/config.php';

$maxDisplay = $config['max_files']();
$images = array_slice(glob($config['image_dir'] . '*'), 0, $maxDisplay);
$docs = glob($config['doc_dir'] . '*');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Gallery</title>
</head>
<body>
<h1>Gallery</h1>
<h2>Images</h2>
<?php foreach ($images as $img): ?>
    <img src="<?php echo 'uploads/imgs/' . basename($img); ?>" style="max-width:200px;">
<?php endforeach; ?>
<h2>Documents</h2>
<ul>
<?php foreach ($docs as $doc): ?>
    <li><a href="<?php echo 'uploads/docs/' . basename($doc); ?>" target="_blank"><?php echo basename($doc); ?></a></li>
<?php endforeach; ?>
</ul>
<p><a href="upload.php">Upload more files</a></p>
</body>
</html>
