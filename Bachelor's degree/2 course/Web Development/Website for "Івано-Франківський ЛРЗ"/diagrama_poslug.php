<?php
function Diagramm($im, $VALUES, $LEGEND, $txt)
{
    global $COLORS, $SHADOWS;
    $black = ImageColorAllocate($im, 0, 0, 0);
/*$im - идентификатор изображения;
$VALUES - массив со значениями;
$LEGEND - массив с подписями.
Получим размеры изображения:*/
    $W = ImageSX($im);
    $H = ImageSY($im);
/*Вывод легенды
Посчитаем количество пунктов, от этого зависит высота легенды*/
    $legend_count = count($LEGEND);
    //Посчитаем максимальную длину пункта, от этого зависит ширина легенды
    $max_length = 0;
    foreach ($LEGEND as $v) if ($max_length < strlen($v)) $max_length = strlen($v);
    //Номер шрифта, котором мы будем выводить легенду. Также получим высоту и ширину символов для шрифта.
    $FONT = 2;
    $font_w = ImageFontWidth($FONT);
    $font_h = ImageFontHeight($FONT);
    //Основные приготовления для выводе легенды закончены, теперь мы можем переходить непосредственно к рисованию. Начнем с рамки вокруг легенды. Рассчитаем ее ширину:
/*Ширина =

(ширина текста (ширина символа * максимальное количество символов)) +
(место для квадратика с цветом (размер квадратика равен высоте шрифта)) +
(отступ от левого края легенды до квадратика с цветом) +
(отступ от квадратика с цветом до текста) +
(отступ от текста для правого края легенды);*/
    $l_width = ($font_w * $max_length) + $font_h + 10 + 5 + 10;
/*Высота =

(высота текста) +
(отступ между текстом и верхним краем) +
(отступ между текстом и нижним краем)*/
    $l_height = $font_h * $legend_count + 10 + 10;
    //Получим координаты верхнего левого угла прямоугольника - границы легенды
    $l_x1 = $W - 10 - $l_width;
    $l_y1 = ($H - $l_height) / 2;
    //Вывод прямоугольника - границы легенды
    ImageRectangle($im, $l_x1, $l_y1, $l_x1 + $l_width, $l_y1 + $l_height, $black);
    //Вывод текст легенды и цветных квадратиков
    $text_x = $l_x1 + 10 + 5 + $font_h;
    $square_x = $l_x1 + 10;
    $y = $l_y1 + 10;
    $i = 0;
    foreach ($LEGEND as $v)
    {
        $dy = $y + ($i * $font_h);
        ImageString($im, $FONT, $text_x, $dy, $v, $black);
        ImageFilledRectangle($im, $square_x + 1, $dy + 1, $square_x + $font_h - 1, $dy + $font_h - 1, $COLORS[$i]);
        ImageRectangle($im, $square_x + 1, $dy + 1, $square_x + $font_h - 1, $dy + $font_h - 1, $black);
        $i++;
    }
/*Вывод круговой диаграммы
Для начала посчитаем сумму всех значений в массиве $VALUES и инициализируем массивы. В массиве $angle будет хранится угловая ширина сектора, а в массиве $anglesum начальный угол каждого сектора. Последним элементов массива $anglesum станет его первый элемент.*/
    $total = array_sum($VALUES);
    $anglesum = $angle = Array(
        0
    );
    $i = 1;
    // Расчет углов
    while ($i < count($VALUES))
    {
        $part = $VALUES[$i - 1] / $total;
        $angle[$i] = floor($part * 360);
        $anglesum[$i] = array_sum($angle);
        $i++;
    }
    $anglesum[] = $anglesum[0];
    //Расчет диаметра
    $diametr = $l_x1 - 10 - 10;
    //Расчет координат центра эллипса
    $circle_x = ($diametr / 2) + 10;
    $circle_y = $H / 2 - 10;
    //Поправка диаметра, если эллипс не помещается по высоте
    if ($diametr > ($H * 2) - 10 - 10) $diametr = ($H * 2) - 20 - 20 - 40;
    //Вывод тени
    for ($j = 20;$j > 0;$j--) for ($i = 0;$i < count($anglesum) - 1;$i++) ImageFilledArc($im, $circle_x, $circle_y + $j, $diametr, $diametr / 2, $anglesum[$i], $anglesum[$i + 1], $SHADOWS[$i], IMG_ARC_PIE);
    //Вывод круговой диаграммы
    for ($i = 0;$i < count($anglesum) - 1;$i++) ImageFilledArc($im, $circle_x, $circle_y, $diametr, $diametr / 2, $anglesum[$i], $anglesum[$i + 1], $COLORS[$i], IMG_ARC_PIE);
    
    $color = ImageColorAllocate($im, 255, 47, 88);
    ImageString($im, 5, 235, 100, $txt, $color);
} /* Конец функции вывода круговой диаграммы */
//Зададим значение и подписи

$fix = $_POST["fix"];
$mod = $_POST["modernization"];
$res = $_POST["restoration"];
$sale = $_POST["sale"];

$VALUES = Array($fix, $mod, $res, $sale);
$LEGEND = Array("Repair", "Modernization", "Restoration", "Sale of locomotives");
//Создадим изображение
header("Content-Type: image/png");
$im = ImageCreate(500, 500);
$txt = $_POST["text_space"];

//Зададим цвет фона. Немного желтоватый, для того, чтобы было видно границы изображения на белом фоне.
$bgcolor = ImageColorAllocate($im, 255, 255, 200);

//Зададим цвета секторов
$COLORS[0] = imagecolorallocate($im, 220, 101, 29);
$COLORS[1] = imagecolorallocate($im, 0, 145, 195);
$COLORS[2] = imagecolorallocate($im, 0, 115, 106);
$COLORS[3] = imagecolorallocate($im, 255, 255, 0);

//Зададим цвета теней секторов
$SHADOWS[0] = imagecolorallocate($im, 170, 51, 0);
$SHADOWS[1] = imagecolorallocate($im, 0, 95, 145);
$SHADOWS[2] = imagecolorallocate($im, 0, 65, 56);
$SHADOWS[3] = imagecolorallocate($im, 87, 41, 24);

//Вызов функции рисования диаграммы
Diagramm($im, $VALUES, $LEGEND, $txt);

//Генерация изображения
ImagePNG($im);
?>
