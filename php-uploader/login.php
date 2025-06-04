<?php
session_start();
$config = include __DIR__ . '/config.php';

if (isset($_POST['logout'])) {
    session_destroy();
    header('Location: index.php');
    exit;
}

$userid = $_POST['userid'] ?? '';
$password = $_POST['password'] ?? '';

if (isset($config['users'][$userid]) && password_verify($password, $config['users'][$userid])) {
    $_SESSION['authenticated'] = $userid;
    header('Location: upload.php');
    exit;
}

header('Location: index.php');
