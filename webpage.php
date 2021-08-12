<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>StockPage Utilizing Database</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
    <script src="index.js"></script>
    <!--import for Chart.js-->





</head>

<body>

<?php
$conn = mysqli_connect("127.0.0.1", "root", "", "test.db");

$sql = "SELECT * FROM stocks2 WHERE ticker = 'AAPL'";
$result = $conn-> query($sql);

if($result-> num_rows>0){
    while($row = $result-> fetch_assoc()){
        echo "<tr><td>". $row["id"]. "</td><td>". $row["price"]."</td></tr>;
    }
}

?>


</body>
</html>
