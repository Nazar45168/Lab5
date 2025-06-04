<?php
session_start();
$config = include __DIR__ . '/config.php';

if (!empty($_SESSION['authenticated'])) {
    echo '<p>You are logged in. <a href="upload.php">Upload files</a></p>';
    echo '<p><a href="gallery.php">View Gallery</a></p>';
    echo '<form method="post" action="login.php"><button type="submit" name="logout">Logout</button></form>';
    exit;
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post" action="login.php">
        <label>User ID: <input type="text" name="userid" required></label><br>
        <label>Password: <input type="password" name="password" required></label><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
