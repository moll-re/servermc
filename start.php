<html>
   <head>
    <title>Activate MC</title>
   </head>

   <body>
     <?php
      $status = 'at rest';
      $hash = '$2y$10$tiWAEQ01XAD1Qgn1J6GFee1A4ZTTBKbHTkF2qORqF/HPGYY5ZEDLC';

      if (isset($_POST['submit'])){
        $pw = $_POST["password"];
        if (password_verify($pw, $hash)) {
          $status = "SUCCESS";
          shell_exec("server_boot.sh");
      } else {
         $status = "try again";
      }
    }
      ?>
     <h1> Start the MC-Server </h1>

     Reminder: ip adress is: <a href="mc.remy-moll.selfhost.eu">mc.remy-moll.selfhost.eu</a>

     <form method="post" action="">
       Password: <input type="password" name="password">
       <br/><input type="submit" value="submit" name="submit">
     </form>
     Status: <?php echo $status; ?>
   </body>
</html>
