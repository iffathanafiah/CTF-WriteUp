# impossibleLogin~.

<?php

/* if (isset($_POST[base64_decode("dXNlcm5hbWU=")]) && isset($_POST[base64_decode("cHdk")])) {
    $yuf85e0677 = $_POST[base64_decode("dXNlcm5hbWU=")];
    $rs35c246d5 = $_POST[base64_decode("cHdk")];
    if ($yuf85e0677 == $rs35c246d5) {
        echo base64_decode("PGJyLz5GYWlsZWQhIE5vIGZsYWcgZm9yIHlvdQ==");
    } else {
        if (sha1($yuf85e0677) === sha1($rs35c246d5)) {
            echo file_get_contents(base64_decode("Li4vZmxhZy50eHQ="));
        } else {
            echo base64_decode("PGJyLz5GYWlsZWQhIE5vIGZsYWcgZm9yIHlvdQ==");
        }
    }
} */

if (isset($_POST["username"]) && isset($_POST["pwd"])) {

    /* $yuf85e0677 = $_POST[base64_decode("dXNlcm5hbWU=")]; */
    $yuf85e0677 = $_POST["username"];

    /* $rs35c246d5 = $_POST[base64_decode("cHdk")]; */
    $rs35c246d5 = $_POST["pwd"];

    if ($yuf85e0677 == $rs35c246d5) {
        echo "<br/>Failed! No flag for you";
    } 
    else {
        if (sha1($yuf85e0677) === sha1($rs35c246d5)) {
            echo file_get_contents("../flag.txt");
        } 
        else {
            echo "<br/>Failed! No flag for you";
        }
    }
}
?>