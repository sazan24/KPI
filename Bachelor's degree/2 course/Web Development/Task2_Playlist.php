<!DOCTYPE html>
<html>
    <head>
      <title>Playlist</title>
    </head>
<body>
    
<form action="Task2_Playlist.php" method="post">
    <p>Сортувати за:</p>
        <input type="submit" name="singer" value="Виконавець">
        <input type="submit" name="year" value="Рік">
        <input type="submit" name="album" value="Альбом">
        <input type="submit" name="song" value="Назва пісні">
</form>

<hr>

<?php 
    $dir = "Songs";
    $files = array_diff(scandir($dir), array(".", ".."));
    
$playlist = array();
foreach($files as $value) {
    $songs = explode("--", $value);
    array_push($playlist, $songs);
   
} 

function sortMatrix_byColumn($array, $column_name) {
    foreach ($array as $key => $row) {
        $column[$key]  = $row[$column_name];
    }
    array_multisort($column, $array);
    return $array;
}

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    if (isset($_POST["singer"])) {
        $new = sortMatrix_byColumn($playlist, "0");
    } elseif (isset($_POST["year"])) {
        $new = sortMatrix_byColumn($playlist, "1");
    } elseif (isset($_POST["album"])) {
        $new = sortMatrix_byColumn($playlist, 2);
    } elseif (isset($_POST["song"])) {
        $new = sortMatrix_byColumn($playlist, 3);
    } elseif (is_null($_POST["singer"])) {
        $new = sortMatrix_byColumn($playlist, 3);
    }
} elseif (True) {
    $new = sortMatrix_byColumn($playlist, 3); 
}

foreach($new as $song) {
    $separated = implode("--", $song);
    echo "<figure> ";
    echo    "<figcaption> $separated </figcaption> ";
    echo    "<audio ";
    echo        "controls ";
    echo        "src='Songs/$separated'> ";
    echo    "</audio> ";
    echo "</figure> ";
    echo "<br>";
}
?>

</body>
</html>

