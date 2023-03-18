
<?php 

function generator_matrix($n, $m) 
{ 
    for ($i = 1; $i <= $n; $i++) { 
        for ($j = 1; $j <= $m; $j++) { 
            $arr[$i][$j] = rand(0, 99); 
        } 
    } 
    return $arr; 
} 
 
function print_matrix($arr, $n, $m) 
{ 
    echo "<table bordercolor = 'red' border = '3px' width = '25%' >"; 
    for ($i = 1; $i <= $n; $i++) { 
        echo "<tr>"; 
        for ($j = 1; $j <= $m; $j++) { 
            echo "<td><div align='center'>" . $arr[$i][$j]. "</div></td>"; 
        } 
        echo "</tr>"; 
    } 
    echo "</table>"; 
} 
 
function search_max_min($arr, $n) 
{ 
    $max_on_rows = []; 
    $min_on_rows = []; 
    for ($i = 1; $i <= $n; $i++) { 
        array_push($max_on_rows, max($arr[$i])); 
        array_push($min_on_rows, min($arr[$i])); 
    } 
    return array(max($max_on_rows), min($min_on_rows)); 
} 
 
function change_max_min_print($arr, $n, $m, $max, $min) 
{ 
    echo "<table bordercolor = 'black' border = '3px' width = '25%'>"; 
    for ($i = 1; $i <= $n; $i++) { 
        echo "<tr>"; 
        for ($j = 1; $j <= $m; $j++) { 
            echo "<td>"; 
            if ($arr[$i][$j] == $max) { 
                echo "<div style = 'color: lime' align = 'center'>" . $arr[$i][$j] = $min . "</div>"; 
            }     
            elseif ($arr[$i][$j] == $min) { 
                echo "<div style = 'color: gold' align = 'center'>" . $arr[$i][$j] = $max . "</div>"; 
            } 
            else {
                echo "<div align = 'center'>" . $arr[$i][$j]. "</div>";
            }
            echo "</td>"; 
        } 
         echo "</tr>"; 
    } 
    echo "</table>"; 
    return $arr; 
} 
 
 
 
 
$i = 20; $j = 20; 
 
$my_matrix = generator_matrix($i, $j); 
print_matrix($my_matrix, $i, $j); 

echo "<br>";

$max_min = search_max_min($my_matrix, $i); 
$new_matrix = change_max_min_print($my_matrix, $i, $j, $max_min[0], $max_min[1]); 
echo "\n"; 
 
 
?>
