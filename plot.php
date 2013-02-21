<?php
$plot = $_GET['plot'];
$connection = mysql_connect("dbserver", "dbuser", "password") or die ("Unable to connect to server");
$db = mysql_select_db("db", $connection) or die ("Unable to select database");


Header ("Content-type: image/png");
// this is the base image
$img = imageCreateFromPNG("blank-graph.png");

$color1 = ImageColorAllocate ($img, 255, 255, 255);
$color2 = ImageColorAllocate ($img, 255, 0, 0);
$color3 = ImageColorAllocate ($img, 0, 0, 255);
$color4 = ImageColorAllocate ($img, 0, 0, 0);

$query = "SELECT glon, glat, j_m_ext, h_m_ext, k_m_ext FROM `2mass_xsc` WHERE k_m_ext < $plot AND cc_flg =0 AND vc = 1 AND cc_flg!='Z'";
$result = mysql_query($query);
while ($row = mysql_fetch_row($result)) {
                $xtmp=$row[0];
                $ytmp=$row[1];
                $jtmp=$row[2];
                $htmp=$row[3];
                $ktmp=$row[4];
                $jh = $jtmp - $htmp;
                $hk = $htmp - $ktmp;

                $y = (200 - ($ytmp*1.85));
                if ($xtmp > 180){
                $x1 = $xtmp - 180;
                $x = 35+($x1*2);
                }
                else                 
                $x = 395 + ($xtmp*2.05);
                
                if ($hk < 0){
                $color = imagecolorallocate($img, 0, 0, 255);
                }elseif ($hk > 0.5) {
                $color = ImageColorAllocate($img, 255, 0, 0);
 }
                else
                $color = ImageColorAllocate($img, 255, 255, 255);
                imagesetpixel($img,$x,$y,$color);
}
$text = $plot."th "."Magnitude";
imagestring($img, 8, 314, 375, $text, $color4);
ImagePng ($img);
ImageDestroy ($img);
?>
